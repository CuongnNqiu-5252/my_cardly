import hashlib
import os
from datetime import timedelta, timezone, datetime
from typing import Optional

import bcrypt
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.database import mongodb

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

ALGORITHM = os.getenv("ALGORITHM", "HS256")


async def valid_user_id(id: str)->bool:
    print(id)
    user = await mongodb.db.users.find_one({"_id": id})
    if user:
        return True
    else:
        return False
async def valid_user_email(email: str) -> dict:
    user = await mongodb.db.users.find_one({"email": email})
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
async def valid_user_exist_email(email: str) -> bool:
    user = await mongodb.db.users.find_one(
        {"email": email}
    )

    return user is not None
def _pre_hash_password(password: str) -> bytes:
    return hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')

def hash_password(password: str) -> str:
    return bcrypt.hashpw(_pre_hash_password(password), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(_pre_hash_password(plain_password), hashed_password.encode('utf-8'))

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES"),))
    )
    return jwt.encode({"sub": subject, "exp": expire}, os.getenv("SECRET_KEY"), algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        secret_key = os.getenv("SECRET_KEY", "your-super-secret-key-for-dev")
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception

        return user_id
    except JWTError:
        raise credentials_exception