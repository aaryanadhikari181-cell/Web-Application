from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.schemas import UserCreate, UserLogin, UserResponse, Token
from app.controllers.auth_controller import (
    create_user, authenticate_user, create_access_token,
    get_current_user, TOKEN_EXPIRE,
)
from app.models import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    """Register a new user account."""
    return create_user(db, payload)


@router.post("/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    """Login with email + password, returns a JWT bearer token."""
    user  = authenticate_user(db, payload.email, payload.password)
    token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=TOKEN_EXPIRE),
    )
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)):
    """Return the currently authenticated user's profile."""
    return current_user
