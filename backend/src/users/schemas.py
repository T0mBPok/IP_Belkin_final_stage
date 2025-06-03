from pydantic import BaseModel

class auth(BaseModel):
    login: str
    password: str