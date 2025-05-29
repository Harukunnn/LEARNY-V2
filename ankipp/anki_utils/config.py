"""Configuration utilities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""

    # TODO: define configuration fields
    debug: bool = False
