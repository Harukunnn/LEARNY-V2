"""Simple in-memory data storage for tests."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from ..models.card import Card
from ..models.deck import Deck


@dataclass
class InMemoryDB:
    """In-memory storage for decks and cards."""

    decks: Dict[int, Deck] = field(default_factory=dict)
    cards: Dict[int, Card] = field(default_factory=dict)
    next_id: int = 1

    def allocate_id(self) -> int:
        ident = self.next_id
        self.next_id += 1
        return ident


db = InMemoryDB()
