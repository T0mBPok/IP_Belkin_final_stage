from src.database import async_session_maker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete


class BaseDAO:
    model = None
    
    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            new_obj = cls.model(**values)
            session.add(new_obj)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return new_obj
        
    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            data = await session.execute(select(cls.model).filter_by(**filter_by))
            return data.scalars().all()
        
    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            conditions = [getattr(cls.model, k) == v for k, v in filter_by.items() if v is not None]
            check = await session.execute(delete(cls.model).where(*conditions))
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return check.rowcount