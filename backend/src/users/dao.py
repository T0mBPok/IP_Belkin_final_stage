from sqlalchemy import select
from src.database import async_session_maker
from src.users.models import User


class UserDAO:
    async def get_user_dao(login: str):
        async with async_session_maker() as session:
            user = await session.execute(select(User).where(User.login == login))
            return user.scalars().one_or_none()
    
    async def find_one_or_none_by_id(data_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(User)
                .where(User.id == data_id)
            )
            return result.scalar_one_or_none()