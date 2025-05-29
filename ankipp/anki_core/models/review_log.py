"""Review log model."""

from __future__ import annotations

from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .card import Card

from .enums import Rating


class ReviewLog(SQLModel, table=True):
    """History of card reviews."""

    id: Optional[int] = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")
    review_time: datetime = Field(default_factory=datetime.utcnow)
    rating: Rating
    interval: int
    ease: float

    card: "Card" = Relationship(back_populates="review_logs")

