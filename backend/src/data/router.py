from src.data.dao import DataDAO
from src.data.logic import add_data_logic
from fastapi import APIRouter, Depends
from src.data.schemas import GetData, AddData, DeleteData
from src.data.rb import RBData
from src.users.dependencies import get_current_user

router = APIRouter(prefix='/data', tags=['Работа с данными'])

@router.get('/', summary='Получить все данные', response_model = list[GetData])
async def get_data(request_body: RBData = Depends(), user: str = Depends(get_current_user)):
    return await DataDAO.get_all_data(**request_body.to_dict())

@router.post('/', summary='Отправить данные формы', response_model=AddData)
async def add_data(form_data: AddData, user: str = Depends(get_current_user)):
    return await add_data_logic(**form_data.model_dump())

@router.delete('/', summary='Удалить данные')
async def delete_data(data: DeleteData, user: str = Depends(get_current_user)):
    return await DataDAO.delete_data(**data.model_dump())