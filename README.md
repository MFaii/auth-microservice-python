
# Auth Microservice (Python + FastAPI)

## Description

This is a simple authentication microservice built with Python, FastAPI, SQLAlchemy, and PostgreSQL. It supports user registration, login, JWT token generation, and user info retrieval.

## Features
- User registration with email and hashed password
- User login with JWT token creation (access token)
- Protected route to get current user info
- Password hashing with bcrypt (via passlib)
- PostgreSQL database integration with SQLAlchemy ORM
- Environment variables management with .env and python-dotenv
- Modular and clean architecture


## Project Structure

```
auth_service/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── users.py             # User routes (register, login, get current user)
│   │       ├── dependencies.py          # Dependencies (get_db, get_current_user, etc.)
│   │       └── api.py                   # API router setup
│   ├── core/
│   │   └── security.py                  # Password hashing & JWT utilities
│   ├── crud/
│   │   └── users.py                    # User CRUD functions
│   ├── db/
│   │   ├── base.py                     # SQLAlchemy base declarative
│   │   └── session.py                  # DB session & engine
│   ├── models/
│   │   └── user.py                     # User model
│   ├── schemas/
│   │   └── user.py                     # Pydantic schemas for User, Token, etc.
│   └── main.py                        # FastAPI app and root router
│
├── test_crud.py                       # Script to test database CRUD operations
├── test_db.py                        # Script to test DB connection & Base metadata
├── .env                             # Environment variables
├── requirements.txt                  # Project dependencies
└── README.md                        # This file
```
## Setup & Installation

### 1.Clone the repo:
```
git clone https://github.com/MFaii/auth-microservice-python.git
cd auth-microservice-python
```
### 2.Create and activate virtual environment:
```
python -m venv venv
source venv/Scripts/activate   # Windows
# or
source venv/bin/activate       # macOS/Linux
```
### 3.Install dependencies:
```
pip install -r requirements.txt
```
### 4.Create .env file with contents:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### 5.Run DB initialization/test scripts if needed:
```
python test_db.py
python test_crud.py
```
### 6.Run the FastAPI app:
```
uvicorn app.main:app --reload
```
## API Reference

#### Register a new user

```
  POST /api/v1/users/register
  Content-Type: application/json
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. User email |
| `password` | `string` | **Required**. User password |

##### Request example:
```
{
  "email": "user@example.com",
  "password": "strongpassword123"
}
```

#### Login user and get token

```
  POST /api/v1/users/login
  Content-Type: application/json
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. User email |
| `password` | `string` | **Required**. User password |

##### Response example:
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5...",
  "token_type": "bearer"
}
```


#### Get current user info

```
  GET /api/v1/users/me
  Authorization: Bearer <access_token>
```

| Parameter |
| :-------- |
| No parameters required. 


##### Response example:
```
{
  "id": 1,
  "email": "user@example.com",
  "is_active": true
}
```
