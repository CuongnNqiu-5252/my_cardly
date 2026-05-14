from fastapi import APIRouter

from app.auth.schemas import UserLogin, Token, UserRegister
from app.auth.service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(request: UserRegister):
    return await register_user(request)
@router.post("/login",response_model=Token)
async def login(request: UserLogin):
    return await login_user(request)