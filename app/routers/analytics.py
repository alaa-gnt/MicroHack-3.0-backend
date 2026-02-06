from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.analytics import DashboardResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter()
