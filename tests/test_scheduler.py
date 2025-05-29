"""Tests for FSRS scheduler."""

from datetime import datetime, timezone

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ankipp.anki_core.models import Card, Rating
from ankipp.anki_core.scheduler import schedule

NOW = datetime(2025, 1, 1, tzinfo=timezone.utc)


def make_card() -> Card:
    return Card()


def test_again_resets_interval() -> None:
    card = make_card()
    schedule(card, Rating.AGAIN, NOW)
    assert card.interval == 1
    assert card.due_date > NOW


def test_hard_decreases_ease() -> None:
    card = make_card()
    schedule(card, Rating.HARD, NOW)
    assert card.interval >= 1
    assert card.ease <= 2.5


def test_good_keeps_ease() -> None:
    card = make_card()
    schedule(card, Rating.GOOD, NOW)
    assert card.interval >= 1
    assert card.ease == 2.5


def test_easy_increases_interval() -> None:
    card = make_card()
    schedule(card, Rating.EASY, NOW)
    assert card.interval > 1
    assert card.ease > 2.5


def test_burnt_sets_huge_interval() -> None:
    card = make_card()
    schedule(card, Rating.BURNT, NOW)
    assert card.interval >= 100000


def test_blackout_resets_everything() -> None:
    card = make_card()
    schedule(card, Rating.BLACKOUT, NOW)
    assert card.interval == 1
    assert card.ease == 1.3

