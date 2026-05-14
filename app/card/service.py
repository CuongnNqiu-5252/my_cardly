from fastapi import HTTPException

from app.auth.dependencies import valid_user_id
from app.card.dependencies import valid_card_id
from app.card.models import Card
from app.card.schemas import CardCreateSchema, CardResponse
from app.database import mongodb


async def create_digital_card(request: CardCreateSchema ,id:str):
    if(await valid_user_id(id)):
        card = Card(**request.dict())
        await mongodb.db.cards.insert_one(card.serializable_dict())
        return CardResponse(**card.dict())
    else:
        raise HTTPException(status_code=400, detail="User does not exist")

