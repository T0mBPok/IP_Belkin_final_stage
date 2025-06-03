from src.database import async_session_maker
from src.data.models import Data
from sqlalchemy import select, delete, and_
from sqlalchemy.exc import SQLAlchemyError


class DataDAO:
    async def get_all_data(**filter_by):
        async with async_session_maker() as session:
            data = await session.execute(select(Data).filter_by(**filter_by))
            return data.scalars().all()
        
    async def add_data(**values):
        async with async_session_maker() as session:
            new_data = Data(**values)
            session.add(new_data)
            try:
                await session.commit()
            except SQLAlchemyError  as e:
                await session.rollback()
                raise e
            return new_data
        
    async def delete_data(**filter_by):
        async with async_session_maker() as session:
            conditions = [getattr(Data, k) == v for k, v in filter_by.items() if v is not None]
            check = await session.execute(delete(Data).where(*conditions))
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return check.rowcount