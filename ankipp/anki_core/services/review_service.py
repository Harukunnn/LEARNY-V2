"""Service to handle card reviews."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlmodel import Session

from ..models import Card, Rating, ReviewLog
from ..scheduler import schedule
from ..storage.repository import CardRepository, ReviewLogRepository


class ReviewService:
    """Business logic for reviewing cards."""

    def __init__(self, session: Session) -> None:
        self.cards = CardRepository(Card, session)
        self.logs = ReviewLogRepository(ReviewLog, session)
        self.session = session

    def review_card(self, card: Card, rating: Rating, reviewed_at: datetime) -> ReviewLog:
        """Review a card and persist the result."""
        schedule(card, rating, reviewed_at)
        log = ReviewLog(
            card_id=card.id,
            card=card,
            rating=rating,
            review_time=reviewed_at,
            interval=card.interval,
            ease=card.ease,
        )
        self.logs.add(log, commit=False)
        self.cards.update(commit=False)
        self.session.commit()
        self.session.refresh(card)
        return log

    def get_due_cards(self, deck_id: Optional[int], before: datetime) -> List[Card]:
        """Return due cards, optionally filtered by deck."""
        cards = self.cards.get_due_cards(before)
        if deck_id is not None:
            cards = [c for c in cards if c.note.deck_id == deck_id]
        return cards

