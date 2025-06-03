from pydantic import BaseModel, EmailStr

class GetData(BaseModel):
    id: int
    name: str
    phone_number: str
    email: str
    
class AddData(BaseModel):
    name: str
    phone_number: str
    email: EmailStr
    
class DeleteData(BaseModel):
    id: int | None = None
    name: str | None = None
    phone_number: str | None = None
    email: str | None = None