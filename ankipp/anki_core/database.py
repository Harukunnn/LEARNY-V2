"""Database helpers using SQLModel."""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from sqlmodel import SQLModel, Session, create_engine


def get_engine(db_path: Path):
    """Return a SQLModel engine for the given path."""
    return create_engine(f"sqlite:///{db_path}", echo=False)


def init_db(engine) -> None:
    """Create all tables."""
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session(engine) -> Iterator[Session]:
    """Provide a transactional session."""
    with Session(engine) as session:
        yield session
        session.commit()

