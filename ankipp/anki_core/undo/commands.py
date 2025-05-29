"""Concrete command implementations for deck and card actions."""

from __future__ import annotations

from typing import cast
from ..models.card import Card
from dataclasses import dataclass

from ..services.deck_service import DeckService
from ..services.card_service import CardService
from .command import Command


@dataclass
class CreateDeckCommand(Command):
    name: str
    deck_id: int | None = None

    def execute(self) -> None:
        self.deck_id = DeckService.create(self.name).id

    def undo(self) -> None:
        if self.deck_id is not None:
            DeckService.delete(self.deck_id)


@dataclass
class RenameDeckCommand(Command):
    deck_id: int
    new_name: str
    old_name: str | None = None

    def execute(self) -> None:
        deck = DeckService.get(self.deck_id)
        self.old_name = deck.name
        DeckService.rename(self.deck_id, self.new_name)

    def undo(self) -> None:
        if self.old_name is not None:
            DeckService.rename(self.deck_id, self.old_name)


@dataclass
class DeleteDeckCommand(Command):
    deck_id: int
    backup: dict[str, object] | None = None

    def execute(self) -> None:
        deck = DeckService.get(self.deck_id)
        self.backup = {"name": deck.name, "cards": DeckService.get_cards(self.deck_id)}
        DeckService.delete(self.deck_id)

    def undo(self) -> None:
        if self.backup:
            name = cast(str, self.backup["name"])
            cards = cast(list[Card], self.backup["cards"])
            restored = DeckService.create(name)
            for card in cards:
                CardService.create(int(restored.id), card.front, card.back)


@dataclass
class CreateCardCommand(Command):
    deck_id: int
    front: str
    back: str
    card_id: int | None = None

    def execute(self) -> None:
        self.card_id = CardService.create(self.deck_id, self.front, self.back).id

    def undo(self) -> None:
        if self.card_id is not None:
            CardService.delete(self.card_id)


@dataclass
class EditCardCommand(Command):
    card_id: int
    new_front: str
    new_back: str
    old_front: str | None = None
    old_back: str | None = None

    def execute(self) -> None:
        card = CardService.get(self.card_id)
        self.old_front = card.front
        self.old_back = card.back
        CardService.edit(self.card_id, self.new_front, self.new_back)

    def undo(self) -> None:
        if self.old_front is not None and self.old_back is not None:
            CardService.edit(self.card_id, self.old_front, self.old_back)


@dataclass
class DeleteCardCommand(Command):
    card_id: int
    backup: dict[str, object] | None = None

    def execute(self) -> None:
        card = CardService.get(self.card_id)
        self.backup = {"deck_id": card.note_id, "front": card.front, "back": card.back}
        CardService.delete(self.card_id)

    def undo(self) -> None:
        if self.backup:
            deck_id = cast(int, self.backup["deck_id"])
            front = cast(str, self.backup["front"])
            back = cast(str, self.backup["back"])
            CardService.create(deck_id, front, back)
