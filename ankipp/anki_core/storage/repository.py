
"""Repository layer wrapping SQLModel sessions."""

from __future__ import annotations

from datetime import datetime
from typing import Generic, Iterable, Optional, TypeVar, Type

from sqlmodel import Session, select

"""Generic repository interface."""

from __future__ import annotations

from typing import Generic, TypeVar


T = TypeVar("T")



class BaseRepository(Generic[T]):
    """Generic repository providing basic CRUD operations."""

    def __init__(self, model: Type[T], session: Session) -> None:
        self.model = model
        self.session = session

    def add(self, obj: T, commit: bool = True) -> T:
        self.session.add(obj)
        if commit:
            self.session.commit()
            self.session.refresh(obj)
        return obj

    def get(self, obj_id: int) -> Optional[T]:
        statement = select(self.model).where(self.model.id == obj_id)
        return self.session.exec(statement).first()

    def list(self) -> Iterable[T]:
        statement = select(self.model)
        return self.session.exec(statement).all()

    def remove(self, obj: T, commit: bool = True) -> None:
        self.session.delete(obj)
        if commit:
            self.session.commit()

    def update(self, commit: bool = True) -> None:
        if commit:
            self.session.commit()



class DeckRepository(BaseRepository):
    """Repository for Deck objects."""

    pass


class NoteRepository(BaseRepository):
    """Repository for Note objects."""

    pass


class CardRepository(BaseRepository):
    """Repository for Card objects."""

    def get_due_cards(self, before: datetime):
        statement = select(self.model).where(self.model.due_date <= before)
        return self.session.exec(statement).all()


class ReviewLogRepository(BaseRepository):
    """Repository for ReviewLog objects."""

    pass


class Repository(Generic[T]):
    """Abstract repository for CRUD operations."""

    # TODO: define CRUD methods
    pass

