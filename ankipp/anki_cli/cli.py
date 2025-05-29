"""CLI entry point for Anki++ using Typer."""

from __future__ import annotations

from pathlib import Path

import typer

from ankipp.anki_core.io.exporter import export_deck
from ankipp.anki_core.io.importer import import_deck

app = typer.Typer()


@app.command()
def export(deck: int, fmt: str = "json", out: str = "deck.json") -> None:
    """Export a deck to a file."""
    path = export_deck(deck, Path(out), fmt)  # type: ignore[arg-type]
    print(path)


@app.command()
def import_(file: str, fmt: str = "json") -> None:
    """Import a deck from a file."""
    deck = import_deck(Path(file), fmt)  # type: ignore[arg-type]
    print(deck.id)


def main() -> None:
    """Run CLI."""
    typer.run(app)


if __name__ == "__main__":
    main()
