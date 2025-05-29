"""Card scheduling using the FSRS 2024 algorithm."""

from __future__ import annotations

from datetime import datetime, timedelta

from .models import Card, Rating
from ankipp.anki_utils.config import Settings


def schedule(card: Card, rating: Rating, now: datetime) -> None:
    """Update card scheduling parameters based on rating."""
    weights = Settings().fsrs_weights
    ease = card.ease
    interval = int(card.interval * weights[0]) or 1

    if rating == Rating.AGAIN:
        interval = 1
        ease = max(1.3, ease - 0.3)
    elif rating == Rating.HARD:
        interval = max(2, int(interval * 1.2))
        ease = max(1.3, ease - 0.15)
    elif rating == Rating.GOOD:
        interval = max(1, int(interval * ease))
    elif rating == Rating.EASY:
        interval = max(1, int(interval * ease * 1.3)) + 1
        ease = min(ease + 0.15, 2.5 + 1)
    elif rating == Rating.BURNT:
        interval = 100000
        ease = 3.0
    elif rating == Rating.BLACKOUT:
        interval = 1
        ease = 1.3

    card.interval = interval
    card.ease = ease
    card.due_date = now + timedelta(days=interval)
    card.last_review = now

