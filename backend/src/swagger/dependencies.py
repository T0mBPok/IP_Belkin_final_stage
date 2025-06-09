from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi import status, Depends
from fastapi.exceptions import HTTPException
from src.config import settings
import secrets


security = HTTPBasic()
def check_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, settings.SWAGGER_LOGIN)
    correct_password = secrets.compare_digest(credentials.password, settings.SWAGGER_PASS)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )