# 📝 FastAPI Notes App (v1)

A backend API for a Notes application built using FastAPI, following a clean layered architecture (Router → Service → Repository). This project demonstrates structured backend design, async programming, and JWT-based authentication.

---

## 🚀 Features

* User registration and login (JWT authentication)
* Create, read, update, and delete notes
* User-specific data isolation
* Async API with FastAPI
* Layered architecture for scalability and maintainability

---

## 🏗️ Project Structure

```
src/
├── core/              # Config & dependency injection
├── database/          # DB session & base setup
├── models/            # SQLAlchemy ORM models
├── repositories/      # Data access layer
├── services/          # Business logic layer
├── routers/           # API endpoints
├── schemas/           # Request/response validation
├── utils/             # Security utilities (JWT, hashing)
├── app.py             # FastAPI application instance

main.py                # Application entry point
```

---

## ⚙️ Tech Stack

* FastAPI
* SQLAlchemy (Async)
* PostgreSQL
* Pydantic
* JWT Authentication
* uv (Python package manager)

---

## 🔧 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/<your-username>/notes-app.git
cd notes-app
```

---

### 2. Install dependencies

```
uv sync
```

---

### 3. Configure environment variables

Create a `.env` file in the root directory:

```
DB_USER=your_user
DB_PASS=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=your_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 4. Run the application

```
uvicorn main:app --reload
```

---

## 📡 API Documentation

Once the server is running:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 🔐 API Endpoints

### Auth

* `POST /auth/register` → Register a new user
* `POST /auth/login` → Authenticate user and get token

### Notes

* `POST /notes/` → Create a note
* `GET /notes/` → Get all notes for current user
* `PUT /notes/{id}` → Update a note
* `DELETE /notes/{id}` → Delete a note

---

## 🧠 Architecture

This project follows a layered architecture:

* **Router Layer** → Handles HTTP requests and responses
* **Service Layer** → Contains business logic
* **Repository Layer** → Handles database interactions

### Why this design?

* Separation of concerns
* Easier testing and debugging
* Scalable for larger systems

---

## 🏷️ Version

**v1** – Initial release with authentication and notes CRUD functionality.

---

## ⚠️ Limitations (v1)

* No pagination or filtering
* Basic error handling
* No logging system
* No automated tests
* No rate limiting

---

## 🚀 Future Improvements

* Pagination & advanced querying
* Centralized exception handling
* Unit and integration testing
* Logging and monitoring
* Caching (Redis)
* Role-based access control

---

## 👤 Author

Vasudeva Reddy
