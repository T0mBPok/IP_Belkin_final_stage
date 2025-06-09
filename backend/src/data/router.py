from src.data.logic import DataLogic
from fastapi import APIRouter, Depends, Path
from src.data.schemas import GetData, AddData
from src.data.rb import RBData
from src.users.dependencies import get_current_user

router = APIRouter(prefix='/data', tags=['Работа с данными'])

@router.get('/', summary='Получить все данные', response_model = list[GetData])
async def get_data(request_body: RBData = Depends(), user: str = Depends(get_current_user)):
    return await DataLogic.get_all(**request_body.to_dict())

@router.post('/', summary='Отправить данные формы', response_model=AddData)
async def add_data(form_data: AddData):
    return await DataLogic.add(**form_data.model_dump())

@router.delete('/{id}', summary='Удалить данные')
async def delete_data(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await DataLogic.delete(id=id)