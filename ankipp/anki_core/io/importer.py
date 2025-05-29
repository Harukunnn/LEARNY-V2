"""Deck import utilities."""

from __future__ import annotations

import json
import sqlite3
import tempfile
import zipfile
from pathlib import Path
from typing import Literal

from ..models.deck import Deck
from ..services.deck_service import DeckService


def import_deck(src: Path, fmt: Literal["json", "apkg"]) -> Deck:
    """Import a deck from the given source file."""
    if fmt == "json":
        data = json.loads(src.read_text())
        deck_dict = data.get("deck", {})
        deck = DeckService.create(deck_dict.get("name", "imported"))
        for card_dict in data.get("cards", []):
            DeckService.add_card(int(deck.id), card_dict["front"], card_dict["back"])
        return deck

    if fmt == "apkg":
        with zipfile.ZipFile(src) as zipf:
            meta = json.loads(zipf.read("meta.json").decode())
            deck = DeckService.create(meta.get("name", "imported"))
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(zipf.read("anki.sqlite"))
                tmp.flush()
                conn = sqlite3.connect(tmp.name)
                for row in conn.execute("SELECT front, back FROM cards"):
                    DeckService.add_card(int(deck.id), row[0], row[1])
                conn.close()
        return deck
    raise ValueError(f"Unsupported format: {fmt}")
