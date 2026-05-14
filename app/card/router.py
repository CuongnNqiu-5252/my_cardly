from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.dependencies import get_current_user
from app.card.schemas import CardCreateSchema, CardResponse
from app.card.service import create_digital_card

router = APIRouter(prefix="/card", tags=["card"])

@router.post("/")
async def create_card(request: CardCreateSchema,userid =Depends(get_current_user)):
    return await create_digital_card(CardResponse(**request.dict()),userid)

