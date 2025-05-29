"""Service layer for card operations."""

from __future__ import annotations

from datetime import datetime

from ..models.card import Card
from ..storage.in_memory import db


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
