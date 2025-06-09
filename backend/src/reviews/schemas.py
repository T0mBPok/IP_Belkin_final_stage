from pydantic import BaseModel

class GetReview(BaseModel):
    id: int
    name: str
    text: str
    
class AddReview(BaseModel):
    name: str
    text: str