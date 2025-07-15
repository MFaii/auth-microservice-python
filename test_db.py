from app.db.session import engine
from app.db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito!")


if __name__ == "__main__":
    create_tables()
