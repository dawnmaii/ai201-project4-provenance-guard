"""
Turning two numbers into one, and one number into something a person can read.

`combine_signals` is where the false-positive trade-off gets made. Everything
after it, the labels and the appeal path, depends on the number it produces.

`score_to_label` turns that number into words a person can read.

The combining rule is written up in the README's Signals and Scoring section,
which names `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score.

    Both inputs point the same way: higher means more likely AI. Your output
    should too.

    Args:
        model_score: from `detector.model_signal` — how predictable the text is.
        style_score: from `stylometry.style_signal` — the shape of the text.

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).

    The rule: average the two signals with equal weight, unless they differ by
    `config.DISAGREEMENT_THRESHOLD` or more, in which case use the lower score.
    The rule and its numbers are in the README's Signals and Scoring section.
    """
    # Rule from the README: a split of 0.30 or more uses the lower score.
    if abs(model_score - style_score) >= config.DISAGREEMENT_THRESHOLD:
        return min(model_score, style_score)
    return (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.

    The label text is written for someone who has never heard the word
    "threshold". All three labels have to be reachable with real text. The
    wording and ranges are in the README's Label Variants section.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", "Probably written by AI."
    if score <= config.HUMAN_THRESHOLD:
        return "human", "Probably written by a human."
    return "unsure", "Not sure if it's human or AI writing."


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
