from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserOut, Token
from app.crud.users import create_user, authenticate_user, get_user_by_email
from app.core.security import create_access_token
from app.db.session import get_db
from app.api.v1.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    print("🔹 Registro iniciado")

    existing_user = get_user_by_email(db, user_in.email)
    print("🔹 Usuario existente:", existing_user)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    user = create_user(db, user_in.email, user_in.password)
    print("🔹 Usuario creado:", user)

    return user


@router.post("/login", response_model=Token)
def login_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(status_code=401, detail="Wrong email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
