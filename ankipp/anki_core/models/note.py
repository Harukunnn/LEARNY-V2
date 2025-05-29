"""Note model."""

from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .deck import Deck
    from .card import Card


class Note(SQLModel, table=True):
    """Representation of a note containing card data."""

    id: Optional[int] = Field(default=None, primary_key=True)
    deck_id: int = Field(foreign_key="deck.id")
    fields: Dict[str, str] = Field(default_factory=dict, sa_column_kwargs={"type_": "JSON"})
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    deck: "Deck" = Relationship(back_populates="notes")
    cards: List["Card"] = Relationship(back_populates="note", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

