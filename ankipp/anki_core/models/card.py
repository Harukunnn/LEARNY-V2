
"""Card model."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Card:
    """Representation of a flash card."""

    id: int = 0
    note_id: int = 0
    front: str = ""
    back: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

from __future__ import annotations
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .note import Note
    from .review_log import ReviewLog

from .enums import CardType
from typing import Optional

from sqlmodel import SQLModel, Field


class Card(SQLModel, table=True):
    """Representation of a flash card."""

    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: int = Field(foreign_key="note.id")
    card_type: CardType = Field(default=CardType.BASIC)
    due_date: datetime = Field(default_factory=datetime.utcnow, index=True)
    ease: float = Field(default=2.5)
    interval: int = Field(default=1)
    last_review: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    note: "Note" = Relationship(back_populates="cards")
    review_logs: List["ReviewLog"] = Relationship(back_populates="card", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

    front: str
    back: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
