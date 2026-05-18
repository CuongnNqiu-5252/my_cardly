import secrets

from fastapi import APIRouter, HTTPException, Query
from starlette.responses import RedirectResponse

from app.auth.dependencies import create_access_token
from app.auth.google import get_google_auth_url, exchange_code_for_token, get_google_user
from app.auth.schemas import UserLogin, Token, UserRegister
from app.auth.service import register_user, login_user
from app.database import mongodb

router = APIRouter(prefix="/auth", tags=["auth"])
_pending_states: set[str] = set()

@router.post("/register")
async def register(request: UserRegister):
    return await register_user(request)
@router.post("/login",response_model=Token)
async def login(request: UserLogin):
    return await login_user(request)

@router.get("/google/login")
async def google_login():
    state = secrets.token_urlsafe(16)
    _pending_states.add(state)
    return RedirectResponse(get_google_auth_url(state))
@router.get("/google/callback")
async def google_callback(code: str = Query(...), state: str = Query(...)):
    if state not in _pending_states:
        raise HTTPException(status_code=400, detail="State không hợp lệ")
    _pending_states.discard(state)

    # Đổi code lấy access token
    token_data = await exchange_code_for_token(code)
    google_user = await get_google_user(token_data["access_token"])

    google_id = google_user["sub"]
    email     = google_user["email"]
    name      = google_user.get("name", "")
    avatar    = google_user.get("picture", "")

    # Upsert user vào MongoDB
    result = await mongodb.db.users.find_one_and_update(
        {"google_id": google_id},
        {"$set": {
            "email":      email,
            "username":   name,
            "avatar_url": avatar,
        }, "$setOnInsert": {
            "google_id":  google_id,
        }},
        upsert=True,
        return_document=True,
    )

    token = create_access_token(str(result["_id"]))
    return {"access_token": token, "token_type": "bearer"}
