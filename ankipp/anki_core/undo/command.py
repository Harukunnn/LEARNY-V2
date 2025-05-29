"""Command pattern base classes."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract command with execute and undo operations."""

    @abstractmethod
    def execute(self) -> None:
        """Perform the command."""
        raise NotImplementedError

    @abstractmethod
    def undo(self) -> None:
        """Undo the command."""
        raise NotImplementedError
