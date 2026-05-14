from motor.motor_asyncio import AsyncIOMotorClient

from app.constants import Environment


class MongoDB:
    client: AsyncIOMotorClient | None = None
    db = None


mongodb = MongoDB()


async def connect_db():
    mongodb.client = AsyncIOMotorClient(
        Environment.MONGO_HOST
    )

    mongodb.db = mongodb.client["cardly"]
    await mongodb.client.admin.command("ping")
    print("db connected")