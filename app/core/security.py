import bcrypt
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import get_settings

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=get_settings().ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, get_settings().SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: bytes):
    encoded_password = plain_password.encode('utf-8')
    return bcrypt.checkpw(password = encoded_password , hashed_password = hashed_password)

def hash_password(password: str):
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=encoded_password, salt=salt)
    return hashed_password
