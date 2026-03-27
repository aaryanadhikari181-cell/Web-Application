from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import TodoCreate, TodoUpdate, TodoResponse
from app.controllers.auth_controller import get_current_user
from app.controllers.todo_controller import (
    get_todos_by_user,
    get_todo_by_id,
    create_todo,
    update_todo,
    delete_todo,
)

router = APIRouter(prefix="/todos", tags=["Todos"])


# ── GET /todos ────────────────────────────────────────────
@router.get("/", response_model=List[TodoResponse])
def list_todos(
    completed: Optional[bool] = None,
    skip:  int = 0,
    limit: int = 100,
    db:   Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Return all todos belonging to the authenticated user.
    - Optional query param: ?completed=true  or  ?completed=false
    - Supports pagination: ?skip=0&limit=20
    """
    return get_todos_by_user(db, current_user, completed=completed, skip=skip, limit=limit)


# ── GET /todos/{id} ───────────────────────────────────────
@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get a single todo by ID (must belong to the authenticated user)."""
    return get_todo_by_id(db, todo_id, current_user)


# ── POST /todos ───────────────────────────────────────────
@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create(
    payload: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new todo for the authenticated user."""
    return create_todo(db, payload, current_user)


# ── PATCH /todos/{id} ─────────────────────────────────────
@router.patch("/{todo_id}", response_model=TodoResponse)
def update(
    todo_id: int,
    payload: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Partially update a todo (title, description, completed).
    Only the fields you send will be updated.
    """
    return update_todo(db, todo_id, payload, current_user)


# ── DELETE /todos/{id} ────────────────────────────────────
@router.delete("/{todo_id}", status_code=status.HTTP_200_OK)
def delete(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a todo by ID (must belong to the authenticated user)."""
    return delete_todo(db, todo_id, current_user)
