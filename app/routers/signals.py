from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.signal import SignalCreate, SignalUpdate, SignalResponse
from app.services.signal_service import SignalService
