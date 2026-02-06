from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.alert import AlertCreate, AlertUpdate, AlertResponse
from app.services.alert_service import AlertService
