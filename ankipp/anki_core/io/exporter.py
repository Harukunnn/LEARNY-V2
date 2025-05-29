"""Deck export utilities."""

from __future__ import annotations

import json
import sqlite3
import tempfile
import zipfile
from pathlib import Path
from typing import Literal

from ..services.deck_service import DeckService


def export_deck(deck_id: int, dst: Path, fmt: Literal["json", "apkg"]) -> Path:
    """Export a deck to ``dst`` in the given format."""
    deck = DeckService.get(deck_id)
    data = {
        "deck": deck.__dict__,
        "cards": [c.__dict__ for c in DeckService.get_cards(deck_id)],
    }

    if fmt == "json":
        dst.write_text(json.dumps(data, default=str))
        return dst

    if fmt == "apkg":
        with zipfile.ZipFile(dst, "w") as zipf:
            zipf.writestr("meta.json", json.dumps(deck.__dict__, default=str))
            # simple sqlite dump with cards table
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                conn = sqlite3.connect(tmp.name)
                c = conn.cursor()
                c.execute("CREATE TABLE cards(id INTEGER, front TEXT, back TEXT)")
                for card in DeckService.get_cards(deck_id):
                    c.execute("INSERT INTO cards VALUES(?,?,?)", (card.id, card.front, card.back))
                conn.commit()
                conn.close()
                zipf.write(tmp.name, "anki.sqlite")
        return dst
    raise ValueError(f"Unsupported format: {fmt}")
