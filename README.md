# Web Application Labs

Labs for Web Application Development course.
**Student:** Aaryan Adhikari
**GitHub:** [aaryanadhikari181-cell](https://github.com/aaryanadhikari181-cell)

---

## Labs Overview

| Lab | Topic | Tech Stack |
|-----|-------|------------|
| [lab1](./lab1) | Portfolio with Calendar | HTML, CSS, JavaScript |
| [lab2](./lab2) | Intro to JavaScript | JavaScript ES6+ |
| [lab3](./lab3) | Login & Register Form | React, State, Components |
| [lab4](./lab4) | Todo CRUD App | React, State Management |
| [lab5](./lab5) | Auth Backend | FastAPI, SQLAlchemy, JWT, Alembic |
| [lab6](./lab6) | Todo API (Auth User) | FastAPI, ORM, Migrations |

---

## LAB 1 — Portfolio with Calendar
A personal portfolio website with an interactive calendar built in vanilla HTML, CSS, and JavaScript.

**How to run:** Open `lab1/index.html` in your browser.

---

## LAB 2 — Intro to JavaScript
An interactive demo page covering core JavaScript ES6+ concepts including `var`/`let`/`const`, functions, arrow functions, objects, `map`, `filter`, and the spread operator.

**How to run:** Open `lab2/index.html` in your browser.

---

## LAB 3 — Login & Register Form (React)
Login and Register forms built with React. Features a custom reusable `Input` component, controlled state, and client-side validation.

**How to run:**
```bash
cd lab3
npm install
npm run dev
```

---

## LAB 4 — Todo CRUD App (React)
A full Create, Read, Update, Delete todo application using React state. Supports filtering, inline editing, and bulk actions.

**How to run:**
```bash
cd lab4
npm install
npm run dev
```

---

## LAB 5 — Auth Backend (FastAPI)
User registration and login REST API with JWT authentication, bcrypt password hashing, SQLAlchemy ORM, and Alembic database migrations.

**How to run:**
```bash
cd lab5
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```
API docs available at: `http://127.0.0.1:8000/docs`

---

## LAB 6 — Todo API with Auth User (FastAPI)
A JWT-protected Todo CRUD API where all todos are scoped to the authenticated user. Built with FastAPI, SQLAlchemy ORM, and Alembic migrations.

**How to run:**
```bash
cd lab6
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```
API docs available at: `http://127.0.0.1:8000/docs`

---

## Repository Structure

```
Web-Application/
├── lab1/         # Portfolio + Calendar (HTML/CSS/JS)
├── lab2/         # Intro to JavaScript
├── lab3/         # React Auth Forms
├── lab4/         # React Todo CRUD
├── lab5/         # FastAPI Auth Backend
├── lab6/         # FastAPI Todo API
└── README.md
```
