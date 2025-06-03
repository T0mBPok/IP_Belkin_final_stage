from src.database import Base, int_pk, str_uniq
from sqlalchemy.orm import Mapped

class Data(Base):
    __tablename__ = 'data'
    id: Mapped[int_pk]
    name: Mapped[str]
    phone_number: Mapped[str_uniq]
    email: Mapped[str_uniq]