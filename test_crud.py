from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.crud.users import create_user, get_user_by_email, authenticate_user

Base.metadata.create_all(bind=engine)


def test_crud():
    db = SessionLocal()

    email = "test@example.com"
    password = "secret123"

    user = create_user(db, email, password)
    print(f"Usuario creado: {user.email} (ID: {user.id})")

    found_user = get_user_by_email(db, email)
    print(f"Usuario encontrado: {found_user.email} (ID: {found_user.id})")

    auth_user = authenticate_user(db, email, password)
    if auth_user:
        print("Autenticación exitosa")
    else:
        print("Autenticación fallida")

    db.close()


if __name__ == "__main__":
    test_crud()
