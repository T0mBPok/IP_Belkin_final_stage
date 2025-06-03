from src.users.dao import UserDAO
from fastapi import HTTPException, status
from src.users.auth import verify_password

async def get_user(login: str, password: str):
    user = await UserDAO.get_user_dao(login=login)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Неправильный логин или пароль')
    return user