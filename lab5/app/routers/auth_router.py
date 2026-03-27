from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.schemas import UserCreate, UserLogin, UserResponse, Token
from app.controllers.auth_controller import (
    create_user,
    authenticate_user,
    create_access_token,
    get_current_user,
    TOKEN_EXPIRE,
)
from app.models import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ── POST /auth/register ───────────────────────────────────
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    - Hashes the password before saving.
    - Returns the created user (without password).
    """
    user = create_user(db, payload)
    return user


# ── POST /auth/login ──────────────────────────────────────
@router.post("/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    """
    Login and receive a JWT access token.
    - Validates email + password.
    - Returns Bearer token valid for ACCESS_TOKEN_EXPIRE_MINUTES.
    """
    user  = authenticate_user(db, payload.email, payload.password)
    token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=TOKEN_EXPIRE),
    )
    return {"access_token": token, "token_type": "bearer"}


# ── GET /auth/me ──────────────────────────────────────────
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """
    Get the currently authenticated user's profile.
    Requires a valid Bearer token in the Authorization header.
    """
    return current_user
