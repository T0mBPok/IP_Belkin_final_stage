from src.database import Base, int_pk
from sqlalchemy.orm import Mapped


class User(Base):
    id: Mapped[int_pk]
    login: Mapped[str]
    password: Mapped[str]