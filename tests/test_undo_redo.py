import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""Tests for undo and redo command manager."""

from ankipp.anki_core.undo import (
    manager,
    CreateDeckCommand,
    CreateCardCommand,
)
from ankipp.anki_core.services.deck_service import DeckService


def test_undo_redo() -> None:
    deck_cmd = CreateDeckCommand("undo_deck")
    manager.do(deck_cmd)
    deck_id = deck_cmd.deck_id
    assert deck_id is not None

    # add 20 cards
    cmds = [CreateCardCommand(deck_id, f"f{i}", f"b{i}") for i in range(20)]
    for cmd in cmds:
        manager.do(cmd)

    assert len(DeckService.get_cards(deck_id)) == 20

    for _ in range(10):
        manager.undo()
    assert len(DeckService.get_cards(deck_id)) == 10

    for _ in range(5):
        manager.redo()
    assert len(DeckService.get_cards(deck_id)) == 15
