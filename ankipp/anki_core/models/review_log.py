"""Review log model."""

from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ReviewLog:
    """History of card reviews."""

    id: int = 0
    card_id: int = 0
    review_time: datetime = field(default_factory=datetime.utcnow)
    rating: int = 0
    interval: int = 0
    ease: float = 0.0

from datetime import datetime

from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .card import Card

from .enums import Rating

from typing import Optional

from sqlmodel import SQLModel, Field



class ReviewLog(SQLModel, table=True):
    """History of card reviews."""

    id: Optional[int] = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")
    review_time: datetime = Field(default_factory=datetime.utcnow)

    rating: Rating
    interval: int
    ease: float

    card: "Card" = Relationship(back_populates="review_logs")


    success: bool


