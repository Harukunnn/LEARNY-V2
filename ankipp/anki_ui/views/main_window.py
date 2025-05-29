
"""Main window view with undo/redo and import/export placeholders."""

"""Main window view."""


from __future__ import annotations


class MainWindow:
    """Placeholder for the main application window."""


    def __init__(self) -> None:
        self.last_action: str | None = None

    def on_undo(self) -> None:
        """Handle undo action."""
        self.last_action = "undo"

    def on_redo(self) -> None:
        """Handle redo action."""
        self.last_action = "redo"

    def on_import(self) -> None:
        """Handle import."""
        self.last_action = "import"

    def on_export(self) -> None:
        """Handle export."""
        self.last_action = "export"

    # TODO: implement PyQt6 window
    pass

