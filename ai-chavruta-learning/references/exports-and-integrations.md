# Exports And Integrations

Read this reference only when the learner asks to export cards, save learning data, track progress, or connect to Anki or another review system.

## Contents

- Capability levels
- Anki TSV
- RemNote
- Portable learning session JSON
- Derived metrics
- Optional AnkiConnect adapter
- Privacy and consent

## Capability Levels

Choose the highest level the host supports without making the core learning session depend on it.

1. **Conversation only:** Render a fenced TSV, JSON, JSONL, or RemNote block for manual copy or import.
2. **File capable:** Write UTF-8 export files after confirming the destination and format.
3. **Tool capable:** Preview and validate the payload, obtain confirmation, then call a local integration such as AnkiConnect.

Never claim a file was written or cards were imported unless the operation completed successfully.

## Anki TSV

Use UTF-8 tab-separated text as the default Anki interchange format. It works without add-ons and keeps the Skill portable.

Prefer this header when the learner has Anki 2.1.54 or later:

```text
#separator:Tab
#html:false
#columns:Front	Back	Tags
[atomic question]	[concise answer]	[topic::subtopic error::type ai-chavruta]
```

Rules:

- Keep one note per line and one knowledge target per note.
- Replace literal tabs and line breaks inside fields with spaces unless HTML output was requested.
- Use space-separated tags with no spaces inside an individual tag.
- Include `ai-chavruta`, a topic tag, and an error-type tag.
- Preserve the exact front field when re-exporting an existing note because Anki commonly uses the first field for duplicate detection and updating.
- Do not invent Anki GUID values. If stable custom identifiers are needed, use a custom first field or store the identifier in the learning-data export.
- Do not generate `.apkg` files unless the host has a tested Anki library and the learner explicitly requests that format.

## RemNote

```text
- [Question] >> [Answer]
  - Tags:: [topic], [error type], ai-chavruta
```

## Portable Learning Session JSON

Use this schema for one completed or paused session. Use ISO 8601 timestamps. Use `null` when a field was not collected; do not infer missing confidence, duration, or outcomes.

```json
{
  "schema_version": "1.0",
  "session_id": "user-provided-or-generated-id",
  "started_at": "2026-01-01T10:00:00+08:00",
  "ended_at": "2026-01-01T10:25:00+08:00",
  "topic": "topic name",
  "goal": "understanding",
  "mode": "diagnostic",
  "learner_state": "review",
  "source_ref": "title, URL, or local reference; omit raw text by default",
  "items": [
    {
      "item_id": "q1",
      "skill_level": "distinction",
      "prompt": "question shown to the learner",
      "initial_response": "learner response",
      "confidence_1_to_5": 3,
      "correctness_0_to_2": 1,
      "reasoning_0_to_2": 1,
      "error_type": "missing-condition",
      "hint_level": 1,
      "revised_response": "revised learner response",
      "repaired": true,
      "transfer_checked": true,
      "transfer_correct": false
    }
  ],
  "summary": {
    "mastered": ["stable point"],
    "unstable": ["point needing review"],
    "misunderstood": ["misconception"],
    "overload_interventions": 0,
    "next_session": ["next action"]
  },
  "cards": [
    {
      "card_id": "c1",
      "front": "atomic question",
      "back": "concise answer",
      "tags": ["ai-chavruta", "topic::subtopic", "error::missing-condition"],
      "source_item_id": "q1"
    }
  ]
}
```

If multiple sessions need append-friendly storage, emit one compact JSON object per line as JSONL.

## Metrics Derived From Session Data

Calculate only when the required fields exist.

- **Repair rate:** repaired weak items / weak items with a repair attempt.
- **Transfer accuracy:** correct transfer checks / completed transfer checks.
- **Calibration gap:** average absolute difference between normalized confidence and correctness.
- **Overload intervention rate:** sessions with at least one overload intervention / completed sessions.
- **Card precision proxy:** cards sourced from documented weak items / all exported cards. This should be 100% under the core protocol.
- **Session completion:** sessions reaching a report / sessions started.

Do not present these as evidence of long-term learning. Retention requires a later recall measurement.

## Optional AnkiConnect Adapter

Use direct import only when all of the following are true:

- The learner explicitly asks for direct Anki import.
- Anki Desktop is running with AnkiConnect installed.
- The host can send HTTP POST requests to `http://127.0.0.1:8765`.
- The learner has approved the deck, note type, fields, tags, and final preview.

Recommended sequence:

1. Call `version` to verify the local service.
2. Read `deckNames`, `modelNames`, and `modelFieldNames` before constructing notes.
3. Show the exact notes and destination deck to the learner.
4. Call `canAddNotes` to identify invalid or duplicate candidates.
5. Import approved candidates with `addNotes`.
6. Report created note IDs and any rejected notes.
7. Save or render the TSV fallback if direct import fails.

When Python 3 is available, prefer the bundled adapter for deterministic validation:

```text
python scripts/anki_connect.py preview path/to/payload.json
python scripts/anki_connect.py check
python scripts/anki_connect.py import path/to/payload.json
python scripts/anki_connect.py import path/to/payload.json --commit
```

The first `import` command performs an AnkiConnect dry run. Add `--commit` only after the learner approves the preview. Add `--create-deck` together with `--commit` only when the learner explicitly wants the named deck created.

Use request version 5 unless the installed AnkiConnect reports otherwise. Keep the service bound to localhost; never ask the learner to expose port 8765 publicly for this workflow.

Example payload shape:

```json
{
  "action": "addNotes",
  "version": 5,
  "params": {
    "notes": [
      {
        "deckName": "AI Chavruta",
        "modelName": "Basic",
        "fields": {
          "Front": "Why is this rule not universal?",
          "Back": "It depends on the boundary condition..."
        },
        "tags": ["ai-chavruta", "error::missing-condition"]
      }
    ]
  }
}
```

## Privacy And Consent

- Store the minimum data required for the learner's stated purpose.
- Prefer topic names and source references over full pasted documents.
- Do not export emotional-distress content, sensitive personal narratives, or crisis details into cards or analytics logs.
- Let the learner inspect and remove items before export.
- Do not send learning data to a remote service without explicit consent and a named destination.
