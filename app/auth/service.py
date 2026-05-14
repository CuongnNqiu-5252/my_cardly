from fastapi import HTTPException
from fastapi_cloud_cli.commands.login import TokenResponse
from starlette import status

from app.auth.dependencies import valid_user_email, verify_password, create_access_token, valid_user_exist_email, \
    hash_password
from app.auth.models import User
from app.auth.schemas import UserLogin, UserRegister, RegisterResponse, Token
from app.database import mongodb


async def register_user(req: UserRegister):
    if await valid_user_exist_email(req.email):
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    user = User(
        email=req.email,
        username=req.username,
        password=hash_password(req.password),
    )

    await mongodb.db.users.insert_one(user.serializable_dict())

    return RegisterResponse(
        username=user.username,
        email=user.email
    )
async def login_user(request: UserLogin):
    user = await valid_user_email(request.email)
    if not user or not verify_password(
        request.password,
        user["password"]

    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        subject=str(user["_id"])
    )

    return Token(access_token=token,token_type="bearer")
