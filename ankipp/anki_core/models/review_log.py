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
