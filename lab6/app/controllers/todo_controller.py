from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models import Todo, User
from app.schemas import TodoCreate, TodoUpdate


def get_todos_by_user(
    db: Session,
    user: User,
    completed: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100,
) -> List[Todo]:
    """Return all todos that belong to the authenticated user.
    Optionally filter by completed status."""
    query = db.query(Todo).filter(Todo.user_id == user.id)
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    return query.order_by(Todo.created_at.desc()).offset(skip).limit(limit).all()


def get_todo_by_id(db: Session, todo_id: int, user: User) -> Todo:
    """Fetch a single todo — only if it belongs to the current user."""
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id={todo_id} not found."
        )
    return todo


def create_todo(db: Session, payload: TodoCreate, user: User) -> Todo:
    """Create a new todo linked to the authenticated user."""
    todo = Todo(
        title=payload.title,
        description=payload.description,
        completed=False,
        user_id=user.id,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session, todo_id: int, payload: TodoUpdate, user: User) -> Todo:
    """Update title, description, or completed status."""
    todo = get_todo_by_id(db, todo_id, user)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo_id: int, user: User) -> dict:
    """Delete a todo — only if it belongs to the authenticated user."""
    todo = get_todo_by_id(db, todo_id, user)
    db.delete(todo)
    db.commit()
    return {"message": f"Todo id={todo_id} deleted successfully."}
