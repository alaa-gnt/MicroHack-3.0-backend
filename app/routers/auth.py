from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.auth_service import AuthService

router = APIRouter()
