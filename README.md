# Provenance Guard

> ## 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>

---

## What This Does

A submission takes these steps:

1. A client sends `POST /submit` with `text` and `creator_id`.
2. `app.py::submit` validates the input. A missing or empty `text`, or a missing `creator_id`, gets a 400. A `text` over 3,000 characters gets a 413. Every error comes back as JSON.
3. Signal one (`detector.py::model_signal`) scores how predictable the text is to a local language model.
4. Signal two (`stylometry.py::style_signal`) scores the shape of the text.
5. `scoring.py::combine_signals` merges the two scores into one score ranging from 0 to 1.
6. `scoring.py::score_to_label` turns that score into a guess (`ai`, `human`, or `unsure`) and a plain-English label.
7. `audit.log_decision` writes the decision to `logs/audit.jsonl`, and the response returns `content_id`, `guess`, `confidence`, `label`, `model_score`, and `style_score`.

**The false-positive trace.** A real writer submits their own work and gets a score of 0.80, which is above the AI threshold. The label they see says the text was probably written by AI. They can `POST /appeal` with their reasoning. The status moves to `under_review` and the appeal is logged next to the original decision.

### Endpoint shapes

`POST /submit`

- In: `{"text": string, "creator_id": string}`. `text` is 3,000 characters at most.
- Out (200):
  - `content_id`: string
  - `guess`: string, one of `ai`, `human`, `unsure`
  - `confidence`: number, 0 to 1
  - `label`: string, the sentence a reader sees
  - `model_score`: number, 0 to 1
  - `style_score`: number, 0 to 1
- Out (error): `{"error", "message"}`, one of:
  - 400 `invalid_json`: body isn't a JSON object
  - 400 `missing_field`: `text` or `creator_id` is absent
  - 400 `empty_text`: `text` is blank
  - 413 `text_too_long`: `text` is over 3,000 characters

`POST /appeal`

- In: `{"content_id": string, "reasoning": string}`. `reasoning` has no length limit yet.
- Out (200):
  - `content_id`: string
  - `status`: string, always `under_review`
  - `message`: string, "Your appeal was recorded. This item is under review."
- Out (error): `{"error", "message"}`, one of:
  - 400 `invalid_json`: body isn't a JSON object
  - 400 `missing_field`: `content_id` or `reasoning` is absent or blank
  - 404 `content_not_found`: no submission has that `content_id`

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a local GPT-2 model. Text the model finds easy to predict scores as more AI-like.

**Why that might differ between human and AI writing:** Generated text tends to pick high-probability words. Human writing makes odder, less predictable choices.

**What it can't see:** Plain or formal human writing is predictable, so it can score as AI. Very short text gives the model too little to work with. Lightly edited AI text can read as human.

### Signal two — the style signal

**What it measures:** Sentence length spread, vocabulary variety (type-token ratio), and punctuation density. It measures shape only, with no understanding of meaning. The style score is built from 1 minus each measure's scaled value, averaged; higher spread and variety, and more punctuation, read as human.

**Why that might differ between human and AI writing:** AI prose tends toward even, mid-length sentences and a narrower vocabulary. Human writing is lumpier.

**What it can't see:** Anything that changes the shape without changing the substance. Adding typos, splitting or merging sentences, or pasting in a quotation can all move it.

### The combining rule

**The rule:** Average the two signals with equal weight. If the two scores differ by 0.30 or more, use the lower score instead of the average. A disagreement never pushes a writer toward AI.

**The numbers:** Model signal weight 0.5, style signal weight 0.5. Disagreement threshold 0.30. All three live in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

The edited AI paragraph (section 3 of `calibration_texts.txt`) scored 0.8072 on the model signal and 0.4958 on the style signal, a split of 0.31. That's over the 0.30 threshold, so the rule used the lower score: 0.4958. A plain average would have given 0.6515, which is just above the 0.64 line and would have been labeled high-confidence AI. The rule keeps this text in the unsure range, which is the outcome I want when the two signals disagree.

**The four calibration inputs** (from `calibration_texts.txt`):

| Input | Model | Style | Split | Combined | Rule used |
| --- | --- | --- | --- | --- | --- |
| Clearly AI | 0.756 | 0.531 | 0.225 | 0.6435 | average |
| Clearly human | 0.4265 | 0.4744 | 0.048 | 0.4505 | average |
| Lightly edited AI | 0.8072 | 0.4958 | 0.311 | 0.4958 | lower score |
| Formal human | 0.4987 | 0.4106 | 0.088 | 0.4546 | average |

Where they agree: the two signals sit within 0.25 of each other on every input except the edited AI text, and the averages for clearly AI and clearly human stay on the same side of the middle. Where they split: the edited AI text, which the model reads as strongly AI and the style signal reads as mid-range. The formal human text is the one I was watching: the model puts it in the middle, not in the AI range, and the style signal reads it as more human than the clearly-human text. The clearly-AI and clearly-human texts combine to only about 0.19 apart, short of the 0.60 spread in criterion 2.

---

## Label Variants

| Label                  | Score range           | The exact text a reader sees               |
|------------------------|-----------------------|--------------------------------------------|
| high-confidence human  | 0.46 or under         | Probably written by a human.               |
| unsure                 | over 0.46, under 0.64 | Not sure if it's human or AI writing.      |
| high-confidence AI     | 0.64 or over          | Probably written by AI.                    |

**Why the thresholds moved from 0.35 and 0.65 to 0.46 and 0.64:** I started with 0.35 and 0.65 as placeholders. When I ran the four calibration texts through the full pipeline, none of them reached a high-confidence label. The clearly-AI text combined to 0.6435, just under 0.65, and the clearly-human text combined to 0.4505, just over 0.35. The signals are compressed toward the middle, so the original lines could never be reached. I moved the human line up to 0.46 so the clearly-human and formal-human texts land in the human label, and the AI line down to 0.64 so the clearly-AI text lands in the AI label.

The cost is on the AI side. Writing that scores between 0.64 and 0.65 is now labeled AI, so some human writing near that score will be flagged. On a writing site, wrongly flagging a writer is the expensive mistake, so this is the setting I'd watch first. I accept the change because the signals can't reach the AI label otherwise, but it's a trade I'm choosing, and unit 8's attack set is where it gets tested.

**Why I worded the "unsure" one this way:**

I don't want to shame the writer for using AI, even if every word was written by them. AI editing could've been used as well. At the same time, if they didn't use AI, the label doesn't ask the writer to do anything, because someone who wrote every word has nothing to fix.

---

## Sample Run

**Deviation from the M3 steps:** I skipped the hardcoded-response step, which asks for a placeholder return to confirm `curl` reaches the route before any logic is added. I built the validation and the signal call directly instead. The route was tested end to end with real requests, but if a failure appears later, I haven't isolated whether the route or the signal caused it.

### A submission

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"Regular exercise offers benefits that extend well beyond physical fitness. It supports cardiovascular health, improves sleep quality, and can reduce feelings of stress. Many people find that a consistent routine makes these benefits easier to maintain over time. Activities such as walking, swimming, and cycling are accessible to most adults and require little specialized equipment. Starting with modest goals and increasing gradually tends to produce the most sustainable results. Ultimately, the best exercise routine is the one a person can keep doing.\",    \"creator_id\": \"tester\"}'

```

```json
{
  "confidence": 0.6435,
  "content_id": "bda7dcdf-9fed-434a-9c15-f6a31cbe8f7e",
  "guess": "ai",
  "label": "Probably written by AI.",
  "model_score": 0.756,
  "style_score": 0.531
}
```

### An appeal

```bash
curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"content_id\": \"bda7dcdf-9fed-434a-9c15-f6a31cbe8f7e\", \"reasoning\": \"I wrote this paragraph myself last week for a class, and I can show my draft.\"}'

```

```json
{
  "content_id": "bda7dcdf-9fed-434a-9c15-f6a31cbe8f7e",
  "message": "Your appeal was recorded. This item is under review.",
  "status": "under_review"
}
```

### What the log shows afterwards

```bash
curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.4958,
      "content_id": "afee98ba-8535-4122-a4cd-49d322695a27",
      "creator_id": "tester",
      "guess": "unsure",
      "label": "Not sure if it's human or AI writing.",
      "model_score": 0.8072,
      "status": "decided",
      "style_score": 0.4958,
      "timestamp": "2026-11-02T00:41:29+00:00"
    },
    {
      "combined_score": 0.45465,
      "content_id": "01d69f1c-3c90-4aa1-919d-f2c2f14eb678",
      "creator_id": "tester",
      "guess": "human",
      "label": "Probably written by a human.",
      "model_score": 0.4987,
      "status": "decided",
      "style_score": 0.4106,
      "timestamp": "2026-11-02T00:41:29+00:00"
    },
    {
      "content_id": "bda7dcdf-9fed-434a-9c15-f6a31cbe8f7e",
      "creator_id": "tester",
      "event": "appeal",
      "reasoning": "I wrote this paragraph myself last week for a class, and I can show my draft.",
      "status": "under_review",
      "timestamp": "2026-11-02T00:41:29+00:00"
    }
  ]
}
```

---

## How I Used AI

### Moment 1

- *What I asked for:*
- *What came back:*
- *What I changed:*

### Moment 2

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```text

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

### Ten audit log entries from the run

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|-----------|--------|-------|-------|-------|---------|
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

### Diagnoses

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
