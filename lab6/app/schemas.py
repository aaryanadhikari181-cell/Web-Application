from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


# ── Auth ──────────────────────────────────────────────────
class UserCreate(BaseModel):
    full_name: str      = Field(..., min_length=3)
    email:     EmailStr
    password:  str      = Field(..., min_length=6)

class UserLogin(BaseModel):
    email:    EmailStr
    password: str

class UserResponse(BaseModel):
    id:        int
    full_name: str
    email:     str
    is_active: bool
    created_at: datetime
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type:   str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[int] = None


# ── Todo ──────────────────────────────────────────────────
class TodoCreate(BaseModel):
    title:       str           = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title:       Optional[str]  = Field(None, min_length=1, max_length=200)
    description: Optional[str]  = None
    completed:   Optional[bool] = None

class TodoResponse(BaseModel):
    id:          int
    title:       str
    description: Optional[str]
    completed:   bool
    user_id:     int
    created_at:  datetime
    updated_at:  Optional[datetime]
    model_config = {"from_attributes": True}
