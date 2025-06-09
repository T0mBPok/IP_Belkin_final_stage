from src.database import Base, int_pk, str_uniq
from sqlalchemy.orm import Mapped

class Review(Base):
    id: Mapped[int_pk]
    