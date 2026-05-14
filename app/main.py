from dotenv import load_dotenv
from fastapi import FastAPI

from app.database import connect_db
from app.auth.router import router as auth_router
from app.card.router import router as card_router

app = FastAPI()
load_dotenv()

app.include_router(auth_router)
app.include_router(card_router)

@app.on_event("startup")
async def startup():
    await connect_db();
    print("db connected")
@app.get("/")
async def root():
    return {"message": "Hello World"}
