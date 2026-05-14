from bson import ObjectId
from fastapi import HTTPException

from app.card.exception import CardNotFound
from app.database import mongodb


async def valid_card_id(id:str)->dict:
    card = await mongodb.db.card.find_one({"_id": ObjectId(id)})
    if card:
       return card
    else:
       raise CardNotFound