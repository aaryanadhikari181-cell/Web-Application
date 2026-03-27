# LAB 5 — FastAPI Auth Backend

User registration and login with JWT authentication, SQLAlchemy ORM, and Alembic migrations.

## Features
- `POST /auth/register` — Register a new user (bcrypt password hashing)
- `POST /auth/login`    — Login and get JWT access token
- `GET  /auth/me`       — Get current user profile (requires Bearer token)

## Project Structure
```
lab5/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── database.py          # DB engine + session + get_db dependency
│   ├── models.py            # SQLAlchemy User model
│   ├── schemas.py           # Pydantic schemas (request/response)
│   ├── controllers/
│   │   └── auth_controller.py  # Password hashing, JWT, DB operations
│   └── routers/
│       └── auth_router.py      # Route handlers
├── alembic/
│   ├── env.py
│   └── versions/
│       └── 0001_create_users.py
├── alembic.ini
├── requirements.txt
└── .env.example
```

## Setup & Run

```bash
# 1. Clone and navigate
cd lab5

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env
# Edit .env and set a strong SECRET_KEY

# 5. Run database migrations
alembic upgrade head

# 6. Start the server
uvicorn app.main:app --reload

# 7. Open API docs
# http://127.0.0.1:8000/docs
```

## API Usage

### Register
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"full_name": "Aaryan Adhikari", "email": "aaryan@example.com", "password": "Secret123"}'
```

### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "aaryan@example.com", "password": "Secret123"}'
# Returns: {"access_token": "eyJ...", "token_type": "bearer"}
```

### Get Profile
```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer eyJ..."
```
