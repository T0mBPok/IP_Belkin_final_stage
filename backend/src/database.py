from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped
from sqlalchemy import func
from src.config import get_db_url


DATABASE_URL = get_db_url()
print(get_db_url())
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


#Настройка аннотаций
int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(DateTime, server_default=func.current_date())]
updated_at = Annotated[datetime, mapped_column(DateTime, server_default=func.current_date(), onupdate=func.current_date())]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    created_at: Mapped[created_at]