"""Scheduling logic for card reviews."""

from __future__ import annotations

from datetime import datetime

from .models.card import Card


class Scheduler:
    """Determine scheduling of card reviews."""

    def get_next_review(self, card: Card) -> datetime:
        """Return the next review time for a given card.

        This is a stub implementation to be completed.
        """
        raise NotImplementedError
