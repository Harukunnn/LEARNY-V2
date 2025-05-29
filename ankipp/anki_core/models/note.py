"""Note model."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Note(SQLModel, table=True):
    """Representation of a note containing card data."""

    id: Optional[int] = Field(default=None, primary_key=True)
    deck_id: int = Field(foreign_key="deck.id")
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
