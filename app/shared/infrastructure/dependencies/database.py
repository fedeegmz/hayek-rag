from typing import AsyncGenerator, Annotated

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClientSession
from pymongo.asynchronous.client_session import AsyncClientSession

from app.shared.infrastructure.mongodb_client import MongoDBClient

db_client = MongoDBClient()


async def _get_db_session() -> AsyncGenerator[AsyncIOMotorClientSession, None]:
    async with db_client.get_session() as session:
        yield session
        session.end_session()


DbSession = Annotated[AsyncClientSession, Depends(_get_db_session)]
