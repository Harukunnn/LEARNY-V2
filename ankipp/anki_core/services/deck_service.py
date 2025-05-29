"""Service layer for deck operations."""

from __future__ import annotations

from datetime import datetime
from typing import List

from ..models.deck import Deck
from ..models.card import Card
from .card_service import CardService
from ..storage.in_memory import db


class DeckService:
    """Business logic related to decks."""

    @staticmethod
    def create(name: str) -> Deck:
        deck = Deck(id=db.allocate_id(), name=name, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.decks[int(deck.id)] = deck
        return deck

    @staticmethod
    def delete(deck_id: int) -> None:
        db.decks.pop(deck_id, None)
        db.cards = {cid: c for cid, c in db.cards.items() if c.note_id != deck_id}

    @staticmethod
    def rename(deck_id: int, new_name: str) -> None:
        deck = DeckService.get(deck_id)
        deck.name = new_name
        deck.updated_at = datetime.utcnow()

    @staticmethod
    def get(deck_id: int) -> Deck:
        return db.decks[deck_id]

    @staticmethod
    def get_cards(deck_id: int) -> List[Card]:
        return [c for c in db.cards.values() if c.note_id == deck_id]

    @staticmethod
    def add_card(deck_id: int, front: str, back: str) -> Card:
        card = CardService.create(deck_id, front, back)
        return card
