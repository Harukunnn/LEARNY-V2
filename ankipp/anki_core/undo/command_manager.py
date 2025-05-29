"""Manage undo and redo stacks."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import List

from .command import Command


class CommandManager:
    """Manages execution history for undo/redo."""

    def __init__(self, capacity: int = 100, dump_path: Path | None = None) -> None:
        self.capacity = capacity
        self._undo_stack: List[Command] = []
        self._redo_stack: List[Command] = []
        self.dump_path = dump_path
        if dump_path and dump_path.exists():
            try:
                with dump_path.open("rb") as fh:
                    self._undo_stack = pickle.load(fh)
            except Exception:
                self._undo_stack = []

    def save(self) -> None:
        """Persist undo stack."""
        if self.dump_path:
            with self.dump_path.open("wb") as fh:
                pickle.dump(self._undo_stack[-self.capacity :], fh)

    def do(self, cmd: Command) -> None:
        """Execute and store a command."""
        cmd.execute()
        self._undo_stack.append(cmd)
        self._redo_stack.clear()
        if len(self._undo_stack) > self.capacity:
            self._undo_stack.pop(0)

    def undo(self) -> None:
        """Undo last command."""
        if not self._undo_stack:
            return
        cmd = self._undo_stack.pop()
        cmd.undo()
        self._redo_stack.append(cmd)

    def redo(self) -> None:
        """Redo last undone command."""
        if not self._redo_stack:
            return
        cmd = self._redo_stack.pop()
        cmd.execute()
        self._undo_stack.append(cmd)
