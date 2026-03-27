from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    full_name       = Column(String(100), nullable=False)
    email           = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active       = Column(Boolean, default=True)
    created_at      = Column(DateTime(timezone=True), server_default=func.now())

    # One user → many todos
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"


class Todo(Base):
    __tablename__ = "todos"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    completed   = Column(Boolean, default=False)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())

    # Foreign key links todo to a user
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner   = relationship("User", back_populates="todos")

    def __repr__(self):
        return f"<Todo id={self.id} title={self.title} user_id={self.user_id}>"
