from src.data.dao import DataDAO
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError


async def add_data_logic(**values):
    try:
        data = await DataDAO.add_data(**values)
    except IntegrityError as e:
        if 'unique constraint' in str(e.orig).lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Данные с таким email или номером телефона уже существуют'
            )
        raise e
    return data