from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


# ── Register ──────────────────────────────────────────────
class UserCreate(BaseModel):
    full_name: str  = Field(..., min_length=3, max_length=100)
    email:     EmailStr
    password:  str  = Field(..., min_length=6)


# ── Login ─────────────────────────────────────────────────
class UserLogin(BaseModel):
    email:    EmailStr
    password: str


# ── Response (never expose hashed_password) ───────────────
class UserResponse(BaseModel):
    id:         int
    full_name:  str
    email:      str
    is_active:  bool
    created_at: datetime

    model_config = {"from_attributes": True}


# ── JWT Token ─────────────────────────────────────────────
class Token(BaseModel):
    access_token: str
    token_type:   str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None
