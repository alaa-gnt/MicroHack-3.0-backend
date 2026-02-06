from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.schemas.pipeline import PipelineResponse
from app.services.pipeline_service import PipelineService
from app.models.user import User

router = APIRouter()

@router.get("/status", response_model=List[PipelineResponse])
def get_pipeline_status(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Placeholder for pipeline status logic
    return []
