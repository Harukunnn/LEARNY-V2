"""Enum definitions for card types and review ratings."""

from __future__ import annotations

from enum import IntEnum


class CardType(IntEnum):
    """Possible types of cards."""

    BASIC = 0
    REVERSIBLE = 1
    CLOZE = 2


class Rating(IntEnum):
    """Possible user ratings after reviewing a card."""

    AGAIN = 0
    HARD = 1
    GOOD = 2
    EASY = 3
    BURNT = 4
    BLACKOUT = 5

