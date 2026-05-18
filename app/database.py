from motor.motor_asyncio import AsyncIOMotorClient

from app.constants import Environment, environment


class MongoDB:
    client: AsyncIOMotorClient | None = None
    db = None


mongodb = MongoDB()


async def connect_db():
    mongodb.client = AsyncIOMotorClient(
        environment.MONGO_HOST,
        serverSelectionTimeoutMS=5000
    )

    mongodb.db = mongodb.client["cardly"]
    mongodb.db.cards.create_index("userd_id", unique=True)
    await mongodb.client.admin.command("ping")
    print("db connected")


async def close_db():

    if mongodb.client:
        mongodb.client.close()

        print("db disconnected")