from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from app.database import connect_db, close_db
from app.auth.router import router as auth_router
from app.card.router import router as card_router
from app.exception import validation_exception_handler

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()

app = FastAPI(lifespan=lifespan)
origins = [
    "http://localhost:5173",  # React Vite
    "http://localhost:3000",  # Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(card_router)
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
