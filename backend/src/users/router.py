from fastapi import Response, APIRouter
from src.users.schemas import auth
from src.users.logic import get_user
from src.users.auth import create_token

router = APIRouter(prefix='/user', tags=['Работа с пользователем'])

@router.post('/', summary='Авторизировать пользователя')
async def auth_user(response: Response, data: auth):
    user = await get_user(**data.model_dump())
    access_token = create_token({"sub": str(user.id)}) # type: ignore
    response.set_cookie(key="access_token", value = access_token, httponly=True, domain='localhost')
    return {"token": access_token}