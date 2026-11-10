# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:53
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `cfd4dfe2-a0e9-4778-a823-55a18ed6eff5` | human | 0.045 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `d7bf0674-76c4-444e-bbae-6e6083f5a637` | human | 0.369 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1fb3dc2c-9395-4574-a02c-7c0fdfff4883` | unsure | 0.637 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `dcdc8cc2-b146-4dc5-834d-b3c917d8ce89` | unsure | 0.637 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e038c0c8-766b-401c-95ed-23c3baa916a7` | human | 0.290 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `263772eb-597b-4bcb-86d6-67d9b3b86160` | unsure | 0.489 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d17025de-4233-4f24-b86b-cfda5ec03370` | unsure | 0.533 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `0d0d3e5b-fc26-4a47-98f4-1008afee71e1` | human | 0.108 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `87634d05-3363-4d58-85f2-e65660880dcc` | unsure | 0.462 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `fa4b173f-38d5-4067-992a-f499739bddfd` | ai | 0.881 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `2c8e048a-6908-4e90-b57b-44d25f316f6b` | unsure | 0.639 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `14f267fc-a487-4727-8f6d-c8331f770c2e` | ai | 0.765 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `87f83095-90cf-4cf4-89d5-bcf5c2f67efe` | ai | 0.792 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b4a6057d-f6e1-4fa6-a27d-9775f56a52d2` | unsure | 0.576 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ed1bb54e-ff02-4bcd-8aab-6a43ebcf466d` | ai | 0.790 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `cdd687a0-e2c4-4550-99b0-161ca40ca432` | unsure | 0.547 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `93cc9fcf-d31a-4acb-bc77-5c40dad9fde9` | unsure | 0.528 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c8ec3474-df49-4a5b-a50f-dda81c76580f` | human | 0.199 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `edba59c2-7e74-4fdd-b6d9-0c584d3ae50c` | human | 0.449 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `20f7f10d-2541-4b1e-94e4-930a2e0f8e03` | human | 0.219 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f22d744e-efa5-42f0-8664-3678a174e52a` | unsure | 0.607 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `352ccb31-8572-4b39-8862-46fd236d0945` | unsure | 0.496 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a9c42673-4fd2-4f4d-82f8-30745b4b4a45` | human | 0.187 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `8d548628-3bd0-4e82-a8e8-24eb0bd719a7` | unsure | 0.592 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `7c2ea99e-8940-48fb-9740-7cf314d1bf53` | human | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `0ce5d9c7-c9bb-4552-9aef-56ccc8372482` | human | 0.000 |  |
| MF05 | malformed | text is a very long single word | 413 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 200 | `532f4166-6422-468d-9fcc-096dcb73f612` | unsure | 0.500 |  |
| MF07 | malformed | text is right-to-left script | 200 | `1d296f06-7f54-490c-9049-ffeac2cb8686` | unsure | 0.500 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a03668b7-73b5-4640-a249-e6a48b5a1686` | human | 0.001 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `24b1e836-1a57-43e5-8868-9c166a6e73bd` | human | 0.001 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc3351b1-2d9c-4ad2-bef4-a7b6562dda66` | human | 0.001 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `89e1fd3e-3618-45f7-a9d1-b22902f06bc3` | human | 0.001 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c9943e5b-4230-4963-8a02-37008550e477` | human | 0.001 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "cfd4dfe2-a0e9-4778-a823-55a18ed6eff5",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.0448,
  "model_score": 0.0448,
  "style_score": 0.5778,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "d7bf0674-76c4-444e-bbae-6e6083f5a637",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.369,
  "model_score": 0.6717,
  "style_score": 0.369,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "1fb3dc2c-9395-4574-a02c-7c0fdfff4883",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.63685,
  "model_score": 0.7852,
  "style_score": 0.4885,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "dcdc8cc2-b146-4dc5-834d-b3c917d8ce89",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6372,
  "model_score": 0.7006,
  "style_score": 0.5738,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e038c0c8-766b-401c-95ed-23c3baa916a7",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2903,
  "model_score": 0.1973,
  "style_score": 0.3833,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "263772eb-597b-4bcb-86d6-67d9b3b86160",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.48905,
  "model_score": 0.6339,
  "style_score": 0.3442,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d17025de-4233-4f24-b86b-cfda5ec03370",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.53325,
  "model_score": 0.6576,
  "style_score": 0.4089,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "0d0d3e5b-fc26-4a47-98f4-1008afee71e1",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.1083,
  "model_score": 0.1083,
  "style_score": 0.5724,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "87634d05-3363-4d58-85f2-e65660880dcc",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4618,
  "model_score": 0.8357,
  "style_score": 0.4618,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "fa4b173f-38d5-4067-992a-f499739bddfd",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8806,
  "model_score": 0.9993,
  "style_score": 0.7619,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "2c8e048a-6908-4e90-b57b-44d25f316f6b",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6393500000000001,
  "model_score": 0.7106,
  "style_score": 0.5681,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "14f267fc-a487-4727-8f6d-c8331f770c2e",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7645500000000001,
  "model_score": 0.8753,
  "style_score": 0.6538,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "87f83095-90cf-4cf4-89d5-bcf5c2f67efe",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7921,
  "model_score": 0.9346,
  "style_score": 0.6496,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "b4a6057d-f6e1-4fa6-a27d-9775f56a52d2",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5755,
  "model_score": 0.9531,
  "style_score": 0.5755,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "ed1bb54e-ff02-4bcd-8aab-6a43ebcf466d",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7901,
  "model_score": 0.9312,
  "style_score": 0.649,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "cdd687a0-e2c4-4550-99b0-161ca40ca432",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5474,
  "model_score": 0.9773,
  "style_score": 0.5474,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "93cc9fcf-d31a-4acb-bc77-5c40dad9fde9",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5285,
  "model_score": 0.9773,
  "style_score": 0.5285,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c8ec3474-df49-4a5b-a50f-dda81c76580f",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.1989,
  "model_score": 0.1989,
  "style_score": 0.5223,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "edba59c2-7e74-4fdd-b6d9-0c584d3ae50c",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.449,
  "model_score": 0.43,
  "style_score": 0.468,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "20f7f10d-2541-4b1e-94e4-930a2e0f8e03",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.219,
  "model_score": 0.0726,
  "style_score": 0.3654,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "f22d744e-efa5-42f0-8664-3678a174e52a",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.60695,
  "model_score": 0.6717,
  "style_score": 0.5422,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "352ccb31-8572-4b39-8862-46fd236d0945",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.49634999999999996,
  "model_score": 0.4997,
  "style_score": 0.493,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "a9c42673-4fd2-4f4d-82f8-30745b4b4a45",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.1873,
  "model_score": 0.7465,
  "style_score": 0.1873,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "8d548628-3bd0-4e82-a8e8-24eb0bd719a7",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.59215,
  "model_score": 0.6081,
  "style_score": 0.5762,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "7c2ea99e-8940-48fb-9740-7cf314d1bf53",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "0ce5d9c7-c9bb-4552-9aef-56ccc8372482",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.0002,
  "model_score": 0.0002,
  "style_score": 0.5,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "532f4166-6422-468d-9fcc-096dcb73f612",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 1.0,
  "style_score": 0.5,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "1d296f06-7f54-490c-9049-ffeac2cb8686",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.986,
  "style_score": 0.5,
  "label": "Not sure if it's human or AI writing.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "a03668b7-73b5-4640-a249-e6a48b5a1686",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0013,
  "model_score": 0.0013,
  "style_score": 0.6667,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "24b1e836-1a57-43e5-8868-9c166a6e73bd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0013,
  "model_score": 0.0013,
  "style_score": 0.6667,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "bc3351b1-2d9c-4ad2-bef4-a7b6562dda66",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0013,
  "model_score": 0.0013,
  "style_score": 0.6667,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "89e1fd3e-3618-45f7-a9d1-b22902f06bc3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0013,
  "model_score": 0.0013,
  "style_score": 0.6667,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c9943e5b-4230-4963-8a02-37008550e477",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0013,
  "model_score": 0.0013,
  "style_score": 0.6667,
  "label": "Probably written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
