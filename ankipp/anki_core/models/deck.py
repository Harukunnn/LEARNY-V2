"""Deck model."""

from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Deck:
    """Representation of a deck of cards."""

    id: int = 0
    name: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .note import Note
from typing import Optional

from sqlmodel import SQLModel, Field

class Deck(SQLModel, table=True):
    """Representation of a deck of cards."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    notes: List["Note"] = Relationship(back_populates="deck", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

