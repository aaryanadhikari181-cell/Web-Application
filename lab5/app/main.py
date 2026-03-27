from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routers.auth_router import router as auth_router

# Create all tables (for dev — in prod use Alembic migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LAB 5 — FastAPI Auth",
    description="User registration and login with JWT authentication.",
    version="1.0.0",
)

# CORS — allow all origins in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "LAB 5 — FastAPI Auth API",
        "docs": "/docs",
        "endpoints": {
            "register": "POST /auth/register",
            "login":    "POST /auth/login",
            "me":       "GET  /auth/me  (requires Bearer token)",
        }
    }
