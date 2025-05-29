"""Tests for the ReviewService."""

from datetime import datetime, timezone

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlmodel import Session, create_engine

from ankipp.anki_core.database import init_db
from ankipp.anki_core.models import Card, Deck, Note, Rating
from ankipp.anki_core.services.review_service import ReviewService

NOW = datetime(2025, 1, 1, tzinfo=timezone.utc)


def setup_db() -> Session:
    engine = create_engine("sqlite:///:memory:")
    init_db(engine)
    return Session(engine)


def create_sample_data(session: Session) -> Card:
    deck = Deck(name="Test")
    note = Note(deck=deck)
    card = Card(note=note)
    session.add(deck)
    session.commit()
    session.refresh(card)
    return card


def test_review_cycle_all_ratings() -> None:
    session = setup_db()
    card = create_sample_data(session)
    service = ReviewService(session)
    ratings = [Rating.AGAIN, Rating.HARD, Rating.GOOD, Rating.EASY, Rating.BURNT, Rating.BLACKOUT]
    for rating in ratings:
        log = service.review_card(card, rating, NOW)
        assert log.rating == rating
    session.close()

