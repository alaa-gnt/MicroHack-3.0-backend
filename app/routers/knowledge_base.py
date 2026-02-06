from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.technology import TechnologyCreate, TechnologyUpdate, TechnologyResponse
from app.services.knowledge_base_service import KnowledgeBaseService
