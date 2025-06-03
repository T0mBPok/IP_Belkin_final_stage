from datetime import timezone, timedelta, datetime
from src.config import get_auth_data
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_token(data: str):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days = 30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, key=auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt

def get_pass_hashed(password: str):
    return pwd_context.hash(password)

def verify_password(plain_pass: str, hashed_password: str):
    return pwd_context.verify(plain_pass, hashed_password)