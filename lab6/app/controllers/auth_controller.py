from datetime import datetime, timedelta
from typing import Optional
import os

from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.database import get_db
from app.models import User
from app.schemas import TokenData, UserCreate

load_dotenv()

SECRET_KEY   = os.getenv("SECRET_KEY", "changeme-secret-key")
ALGORITHM    = os.getenv("ALGORITHM", "HS256")
TOKEN_EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    payload = data.copy()
    expire  = datetime.utcnow() + (expires_delta or timedelta(minutes=TOKEN_EXPIRE))
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, payload: UserCreate) -> User:
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered.")
    user = User(
        full_name=payload.full_name,
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )
    db.add(user); db.commit(); db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str) -> User:
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload  = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id  = payload.get("sub")
        if user_id is None: raise credentials_exc
        token_data = TokenData(user_id=int(user_id))
    except JWTError:
        raise credentials_exc
    user = get_user_by_id(db, token_data.user_id)
    if user is None: raise credentials_exc
    return user
