#!/usr/bin/env python3
"""Preview, validate, and optionally import AI Chavruta notes via AnkiConnect."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


API_VERSION = 5
DEFAULT_URL = "http://127.0.0.1:8765"


class AnkiConnectError(RuntimeError):
    pass


def call(url: str, action: str, params: dict | None = None) -> object:
    payload = json.dumps(
        {"action": action, "version": API_VERSION, "params": params or {}},
        ensure_ascii=False,
    ).encode("utf-8")
    request = Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise AnkiConnectError(f"AnkiConnect request failed: {exc}") from exc

    if not isinstance(data, dict) or "error" not in data or "result" not in data:
        raise AnkiConnectError("AnkiConnect returned an unexpected response shape")
    if data["error"]:
        raise AnkiConnectError(str(data["error"]))
    return data["result"]


def require_local_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
        raise AnkiConnectError("Only a local HTTP AnkiConnect URL is allowed")


def load_payload(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AnkiConnectError(f"Could not read payload: {exc}") from exc

    if not isinstance(data, dict):
        raise AnkiConnectError("Payload root must be a JSON object")

    deck = data.get("deckName")
    model = data.get("modelName")
    notes = data.get("notes")
    if not isinstance(deck, str) or not deck.strip():
        raise AnkiConnectError("deckName must be a non-empty string")
    if not isinstance(model, str) or not model.strip():
        raise AnkiConnectError("modelName must be a non-empty string")
    if not isinstance(notes, list) or not notes:
        raise AnkiConnectError("notes must be a non-empty array")

    normalized = []
    for index, note in enumerate(notes, start=1):
        if not isinstance(note, dict):
            raise AnkiConnectError(f"notes[{index}] must be an object")
        fields = note.get("fields")
        tags = note.get("tags", [])
        if not isinstance(fields, dict) or not fields:
            raise AnkiConnectError(f"notes[{index}].fields must be a non-empty object")
        if not all(isinstance(key, str) and isinstance(value, str) for key, value in fields.items()):
            raise AnkiConnectError(f"notes[{index}].fields keys and values must be strings")
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            raise AnkiConnectError(f"notes[{index}].tags must be an array of strings")
        if any(not tag or any(character.isspace() for character in tag) for tag in tags):
            raise AnkiConnectError(f"notes[{index}].tags must be non-empty and contain no spaces")
        normalized.append(
            {
                "deckName": deck,
                "modelName": model,
                "fields": fields,
                "tags": tags,
            }
        )

    return {"deckName": deck, "modelName": model, "notes": normalized}


def check_environment(url: str) -> dict:
    return {
        "version": call(url, "version"),
        "decks": call(url, "deckNames"),
        "models": call(url, "modelNames"),
    }


def validate_notes(url: str, payload: dict, create_deck: bool) -> tuple[list, list]:
    environment = check_environment(url)
    deck = payload["deckName"]
    model = payload["modelName"]

    if model not in environment["models"]:
        raise AnkiConnectError(f"Anki note type does not exist: {model}")
    if deck not in environment["decks"]:
        if not create_deck:
            raise AnkiConnectError(
                f"Anki deck does not exist: {deck}. Use --create-deck to create it explicitly."
            )
        call(url, "createDeck", {"deck": deck})

    model_fields = call(url, "modelFieldNames", {"modelName": model})
    for index, note in enumerate(payload["notes"], start=1):
        missing = [field for field in model_fields if field not in note["fields"]]
        extra = [field for field in note["fields"] if field not in model_fields]
        if missing or extra:
            raise AnkiConnectError(
                f"notes[{index}] field mismatch; missing={missing}, extra={extra}"
            )

    allowed = call(url, "canAddNotes", {"notes": payload["notes"]})
    accepted = [note for note, can_add in zip(payload["notes"], allowed) if can_add]
    rejected = [
        {"index": index, "front": next(iter(note["fields"].values())), "reason": "duplicate-or-invalid"}
        for index, (note, can_add) in enumerate(zip(payload["notes"], allowed), start=1)
        if not can_add
    ]
    return accepted, rejected


def print_json(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL, help="Local AnkiConnect URL")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check", help="Check the local AnkiConnect service")

    preview = subparsers.add_parser("preview", help="Validate and print a JSON payload offline")
    preview.add_argument("input", type=Path)

    import_parser = subparsers.add_parser(
        "import", help="Validate notes with AnkiConnect; write only with --commit"
    )
    import_parser.add_argument("input", type=Path)
    import_parser.add_argument("--create-deck", action="store_true")
    import_parser.add_argument("--commit", action="store_true")

    args = parser.parse_args()
    try:
        require_local_url(args.url)
        if args.command == "check":
            print_json(check_environment(args.url))
            return 0

        payload = load_payload(args.input)
        if args.command == "preview":
            print_json(payload)
            return 0

        if args.create_deck and not args.commit:
            raise AnkiConnectError("--create-deck requires --commit because deck creation is a write")
        accepted, rejected = validate_notes(args.url, payload, args.create_deck)
        result = {
            "commit": args.commit,
            "accepted": len(accepted),
            "rejected": rejected,
            "created_note_ids": [],
        }
        if args.commit and accepted:
            result["created_note_ids"] = call(args.url, "addNotes", {"notes": accepted})
        print_json(result)
        return 0
    except AnkiConnectError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
