"""Generic repository interface."""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T]):
    """Abstract repository for CRUD operations."""

    # TODO: define CRUD methods
    pass
