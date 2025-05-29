import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""Tests for import and export utilities."""

from pathlib import Path

from ankipp.anki_core.services.deck_service import DeckService
from ankipp.anki_core.services.card_service import CardService
from ankipp.anki_core.io.exporter import export_deck
from ankipp.anki_core.io.importer import import_deck


def setup_deck() -> int:
    deck = DeckService.create("test")
    CardService.create(deck.id, "front1", "back1")
    CardService.create(deck.id, "front2", "back2")
    return deck.id


def test_export_import_json(tmp_path: Path) -> None:
    deck_id = setup_deck()
    out = tmp_path / "deck.json"
    export_deck(deck_id, out, "json")
    new_deck = import_deck(out, "json")
    assert len(DeckService.get_cards(new_deck.id)) == 2


def test_export_import_apkg(tmp_path: Path) -> None:
    deck_id = setup_deck()
    out = tmp_path / "deck.apkg"
    export_deck(deck_id, out, "apkg")
    new_deck = import_deck(out, "apkg")
    assert len(DeckService.get_cards(new_deck.id)) == 2
