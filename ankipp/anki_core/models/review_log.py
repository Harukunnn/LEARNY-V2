"""Review log model."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class ReviewLog(SQLModel, table=True):
    """History of card reviews."""

    id: Optional[int] = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")
    review_time: datetime = Field(default_factory=datetime.utcnow)
    success: bool
