# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-22 22:25
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `d273ed05-3f4b-4ec7-bccd-3e82e815424e` | unsure | 0.571 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `86582045-e2ca-4084-a668-dca74b00f71e` | unsure | 0.416 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `70e9b070-7cca-4686-9687-fcd77cb661d1` | unsure | 0.530 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `4bd20dd6-5cd7-4f16-af61-2a9ae5e16195` | ai | 0.795 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `af2ef18c-2bda-4b96-a241-6d2780510c2a` | human | 0.221 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `aa008757-f445-40f9-9fa1-01176c3c5906` | unsure | 0.406 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e7dbd8cf-69e7-4ad6-a8cc-75787aca4b38` | unsure | 0.481 | BROKE |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8c549589-3ba2-494b-a4de-9374aa6ae921` | unsure | 0.570 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `4025994e-9f11-4c46-86da-82e4aad3acf8` | ai | 0.808 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `66131e93-449c-4675-9419-dcd035d577b6` | unsure | 0.567 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `ad29cfea-16a3-4db5-a626-73260cae021d` | ai | 0.832 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `e2aae6e4-bbaa-49c5-b009-ec1342fa97b1` | ai | 0.782 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `96a16aee-94b3-429e-9c01-93195d244dbf` | ai | 0.760 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `3b05ef97-005b-4e9f-8c28-210b600aabd9` | ai | 0.828 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `ef3cf4de-7d39-43d3-9a9c-85b45ca07bf1` | unsure | 0.641 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `182ecb5e-9f24-4b06-91dc-d797d07b2ef3` | unsure | 0.558 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7382feca-8268-4f46-bba1-08b2f8d66895` | human | 0.356 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `956512b4-9456-4f6a-8ca7-02e8e97d9f3c` | human | 0.197 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f104dcdf-e3b7-4223-9d98-64bc1f630c45` | unsure | 0.612 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `df5f673e-e588-45e2-ac09-4043c30352f3` | unsure | 0.465 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ea988048-8084-4e7c-8e4c-9547ddd1cc6a` | unsure | 0.441 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `930e4159-055d-41e5-9af3-7a1647dda55f` | unsure | 0.549 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "d273ed05-3f4b-4ec7-bccd-3e82e815424e",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5707,
  "model_score": 0.1635,
  "style_score": 0.9779,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "86582045-e2ca-4084-a668-dca74b00f71e",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4159,
  "model_score": 0.5943,
  "style_score": 0.2375,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "70e9b070-7cca-4686-9687-fcd77cb661d1",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5299,
  "model_score": 0.6662,
  "style_score": 0.3936,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "4bd20dd6-5cd7-4f16-af61-2a9ae5e16195",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.7955,
  "model_score": 0.6114,
  "style_score": 0.9796,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
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
  "content_id": "af2ef18c-2bda-4b96-a241-6d2780510c2a",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.221,
  "model_score": 0.3212,
  "style_score": 0.1208,
  "label": "We think this was probably written by a person.",
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
  "content_id": "aa008757-f445-40f9-9fa1-01176c3c5906",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4059,
  "model_score": 0.5727,
  "style_score": 0.2392,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "e7dbd8cf-69e7-4ad6-a8cc-75787aca4b38",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4806,
  "model_score": 0.5862,
  "style_score": 0.375,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "8c549589-3ba2-494b-a4de-9374aa6ae921",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5701,
  "model_score": 0.7042,
  "style_score": 0.4359,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "4025994e-9f11-4c46-86da-82e4aad3acf8",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8078,
  "model_score": 0.9792,
  "style_score": 0.6365,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
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
  "content_id": "66131e93-449c-4675-9419-dcd035d577b6",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5673,
  "model_score": 0.6175,
  "style_score": 0.5171,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "ad29cfea-16a3-4db5-a626-73260cae021d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.8316,
  "model_score": 0.7387,
  "style_score": 0.9244,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
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
  "content_id": "e2aae6e4-bbaa-49c5-b009-ec1342fa97b1",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7824,
  "model_score": 0.8051,
  "style_score": 0.7596,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
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
  "content_id": "96a16aee-94b3-429e-9c01-93195d244dbf",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7601,
  "model_score": 0.8329,
  "style_score": 0.6874,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
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
  "content_id": "3b05ef97-005b-4e9f-8c28-210b600aabd9",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8281,
  "model_score": 0.8005,
  "style_score": 0.8558,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
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
  "content_id": "ef3cf4de-7d39-43d3-9a9c-85b45ca07bf1",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6414,
  "model_score": 0.8814,
  "style_score": 0.4015,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "182ecb5e-9f24-4b06-91dc-d797d07b2ef3",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5577,
  "model_score": 0.8816,
  "style_score": 0.2338,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "7382feca-8268-4f46-bba1-08b2f8d66895",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3563,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We think this was probably written by a person.",
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
  "content_id": "956512b4-9456-4f6a-8ca7-02e8e97d9f3c",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1972,
  "model_score": 0.2044,
  "style_score": 0.19,
  "label": "We think this was probably written by a person.",
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
  "content_id": "f104dcdf-e3b7-4223-9d98-64bc1f630c45",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.6119,
  "model_score": 0.5943,
  "style_score": 0.6296,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "df5f673e-e588-45e2-ac09-4043c30352f3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4647,
  "model_score": 0.4998,
  "style_score": 0.4295,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "ea988048-8084-4e7c-8e4c-9547ddd1cc6a",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4406,
  "model_score": 0.6401,
  "style_score": 0.2411,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "content_id": "930e4159-055d-41e5-9af3-7a1647dda55f",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5491,
  "model_score": 0.5583,
  "style_score": 0.5399,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
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
  "status": 400,
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

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
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

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
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

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
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

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
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
