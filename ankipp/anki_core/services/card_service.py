"""Service layer for card operations."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from ..models import Card, CardType, Note


class CardService:
    """Business logic related to cards."""

    def create_card(
        self, note: Note, card_type: CardType, initial_due: Optional[datetime] = None
    ) -> Card:
        """Instantiate a card for a given note."""
        card = Card(
            note_id=note.id,
            note=note,
            card_type=card_type,
            due_date=initial_due or datetime.utcnow(),
        )
        note.cards.append(card)
        return card

