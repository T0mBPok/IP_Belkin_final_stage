from src.users.dependencies import get_current_user
from src.reviews.dao import ReviewDAO
from fastapi import APIRouter, Depends, Path
from src.reviews.schemas import GetReview, AddReview
from src.reviews.rb import RBReview

router = APIRouter(prefix='/reviews', tags=['Работа с отзывами'])

@router.get('/', summary='Получить отзывы', response_model=list[GetReview])
async def get_reviews(request_body: RBReview = Depends(), user: str = Depends(get_current_user)):
    return await ReviewDAO.get_all(**request_body.to_dict())

@router.post('/', summary='Отправить отзыв', response_model=AddReview)
async def add_data(form_data: AddReview):
    return await ReviewDAO.add(**form_data.model_dump())

@router.delete('/{id}', summary='Удалить отзыв')
async def delete_data(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await ReviewDAO.delete(id=id)