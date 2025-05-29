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
