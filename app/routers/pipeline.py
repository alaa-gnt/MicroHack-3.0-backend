from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.pipeline import PipelineResponse
from app.services.pipeline_service import PipelineService

router = APIRouter()
