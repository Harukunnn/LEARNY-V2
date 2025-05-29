"""Service layer for card operations."""

from __future__ import annotations

from datetime import datetime

from ..models.card import Card
from ..storage.in_memory import db


from datetime import datetime
from typing import Optional

from ..models import Card, CardType, Note



class CardService:
    """Business logic related to cards."""


    @staticmethod
    def create(deck_id: int, front: str, back: str) -> Card:
        card = Card(
            id=db.allocate_id(),
            note_id=deck_id,
            front=front,
            back=back,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.cards[int(card.id)] = card
        return card

    @staticmethod
    def delete(card_id: int) -> None:
        db.cards.pop(card_id, None)

    @staticmethod
    def edit(card_id: int, front: str, back: str) -> None:
        card = CardService.get(card_id)
        card.front = front
        card.back = back
        card.updated_at = datetime.utcnow()

    @staticmethod
    def get(card_id: int) -> Card:
        return db.cards[card_id]


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


    # TODO: implement methods for card management
    pass

