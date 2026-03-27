# LAB 6 — FastAPI Todo API (Auth User)

Todo CRUD REST API where all todos are scoped to the authenticated user. Built with FastAPI, SQLAlchemy ORM, and Alembic migrations.

## Features
- JWT-protected endpoints — all routes require a Bearer token
- Todos are filtered by `user_id` of the authenticated user
- Full CRUD: list, get, create, update (PATCH), delete
- Optional filter by completed status: `GET /todos?completed=true`
- Pagination: `GET /todos?skip=0&limit=20`

## Project Structure
```
lab6/
├── app/
│   ├── main.py                      # FastAPI app + router registration
│   ├── database.py                  # Engine, session, get_db dependency
│   ├── models.py                    # User + Todo SQLAlchemy models (with relationship)
│   ├── schemas.py                   # Pydantic request/response schemas
│   ├── controllers/
│   │   ├── auth_controller.py       # JWT, password hashing, get_current_user
│   │   └── todo_controller.py       # Todo DB operations filtered by user
│   └── routers/
│       ├── auth_router.py           # POST /auth/register, /login; GET /auth/me
│       └── todo_router.py           # GET/POST/PATCH/DELETE /todos
├── alembic/
│   ├── env.py
│   └── versions/
│       └── 0001_create_users_todos.py
├── alembic.ini
├── requirements.txt
└── .env.example
```

## Setup & Run
```bash
cd lab6
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # Edit .env — set a strong SECRET_KEY
alembic upgrade head
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs

## API Endpoints

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| POST | /auth/register | ❌ | Register new user |
| POST | /auth/login | ❌ | Login → get JWT token |
| GET | /auth/me | ✅ | Get current user |
| GET | /todos | ✅ | List all my todos |
| GET | /todos/{id} | ✅ | Get one todo |
| POST | /todos | ✅ | Create a todo |
| PATCH | /todos/{id} | ✅ | Update a todo |
| DELETE | /todos/{id} | ✅ | Delete a todo |

## Example Usage
```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"full_name":"Aaryan Adhikari","email":"aaryan@example.com","password":"Secret123"}'

# Login → copy the access_token
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"aaryan@example.com","password":"Secret123"}'

# Create a todo
curl -X POST http://localhost:8000/todos \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy groceries","description":"Milk, bread, eggs"}'

# List todos
curl http://localhost:8000/todos \
  -H "Authorization: Bearer YOUR_TOKEN"

# List only active todos
curl "http://localhost:8000/todos?completed=false" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Mark as complete
curl -X PATCH http://localhost:8000/todos/1 \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete
curl -X DELETE http://localhost:8000/todos/1 \
  -H "Authorization: Bearer YOUR_TOKEN"
```
