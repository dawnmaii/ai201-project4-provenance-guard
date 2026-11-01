# Acceptance criteria — Provenance Guard

---

## 1. False positives <= 3

The number of false positives labeled high-confidence AI is at most 3 out of the 10 texts I wrote myself.

**Why this target:** If a human's writing is flagged as "high-confidence AI", they may lose trust in the application and won't bother to submit more of their original work for the application. 3 allows for edge cases to be considered (such as AI editing being used). Anything less will not allow for AI-assisted human writing that should still count, anything more will mislabel AI writing as human.

---

## 2. Score spread between AI- and human-written text should be at a minimum gap of 0.60

The score spread between my 3 clearly-AI texts and my 3 clearly-human texts is at least 0.60. The gap will be measured by calculating lowest AI text score - highest human text score. If the gap is negative, that means the groups overlap.

**Why this target:**  A lower score spread makes it harder for the application to tell the two groups of text apart. It would mislabel text that a human writer wrote as AI, forcing them to sound more like AI to fix the error.

---

## 3. In `scenarios.py`, three texts should be labeled as AI, two texts should be labeled as unsure, and three texts should be labeled as human

All eight texts should receive their expected label. 

**Why this target:** Having two texts labeled as "unsure" allows us to see whether we need to tweak the score spread and where the uncertainty lies in those two texts. Without the correct label, writers are not informed about where their writing stands.

---

## 4. Appeal path should be 100%

Of 10 appeals sent to `POST /appeal` with a real `content_id`, 10 set the status to `under_review` and wrote an entry to the audit log after checking `GET /log`.

**Why this target:** Assuming correct input, the application should be following a deterministic path 100% of the time. If an appeal drops without a record, the writer will either give up on submitting or try again, resulting in multiple duplicate requests.

---

## 5. Correct status codes for bad inputs

For 8 bad-input requests sent (see `scenarios.py`), all 8 return the status code and error name listed below based on their type and where the request was sent:

`/submit`

- 400 `invalid_json`: body isn't a JSON object
- 400 `missing_field`: `text` or `creator_id` is absent
- 400 `empty_text`: `text` is blank
- 413 `text_too_long`: `text` is over 3,000 characters

`/appeal`

- 404 `content_not_found`: unknown IDs

**Why this target:** It's important that bad input is labeled with the correct status code for easy troubleshooting and communication to the user, so that such input is quickly corrected before being resubmitted. A writer needs to know whether it's the system's fault or their own fault that their writing is not accepted as valid input.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
