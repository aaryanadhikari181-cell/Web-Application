from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routers.auth_router import router as auth_router
from app.routers.todo_router import router as todo_router

# Create all tables (dev only — use Alembic in production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LAB 6 — FastAPI Todo API",
    description="Todo CRUD API with JWT auth. Todos are scoped to the authenticated user.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(todo_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "LAB 6 — FastAPI Todo API",
        "docs": "/docs",
        "endpoints": {
            "register":      "POST   /auth/register",
            "login":         "POST   /auth/login",
            "me":            "GET    /auth/me",
            "list todos":    "GET    /todos",
            "get todo":      "GET    /todos/{id}",
            "create todo":   "POST   /todos",
            "update todo":   "PATCH  /todos/{id}",
            "delete todo":   "DELETE /todos/{id}",
        },
    }
