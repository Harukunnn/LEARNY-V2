"""Configuration utilities."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Settings:
    """Application settings including FSRS weights."""

    fsrs_weights: List[float] = field(
        default_factory=lambda: [
            0.921, 0.5, 4.83, 0.307, 1.39, 1.26, 0.328, 1.1,
            1.39, 0.94, 2.2, 0.5, 1.22, 1.01, 0.7, 2.2, 1.03
        ]
    )
    request_retention: float = 0.9

