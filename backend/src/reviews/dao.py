from src.dao.base import BaseDAO
from src.reviews.models import Review

class ReviewDAO(BaseDAO):
    model = Review