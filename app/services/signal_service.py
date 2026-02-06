from typing import List, Optional
from sqlalchemy.orm import Session
import uuid
from datetime import datetime

from app.models.signal import Signal
from app.schemas.signal import SignalCreate, SignalUpdate

class SignalService:
    @staticmethod
    def get_signal(db: Session, signal_id: str) -> Optional[Signal]:
        return db.query(Signal).filter(Signal.id == signal_id).first()

    @staticmethod
    def get_signals(db: Session, skip: int = 0, limit: int = 100) -> List[Signal]:
        return db.query(Signal).offset(skip).limit(limit).all()

    @staticmethod
    def create_signal(db: Session, signal_in: SignalCreate) -> Signal:
        db_signal = Signal(
            id=str(uuid.uuid4()),
            **signal_in.model_dump()
        )
        db.add(db_signal)
        db.commit()
        db.refresh(db_signal)
        return db_signal
