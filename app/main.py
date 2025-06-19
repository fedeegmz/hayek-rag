from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.shared.infrastructure.dependencies.database import db_client
from app.shared.infrastructure.exception_handler import exception_handler


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    await db_client.connect()
    yield
    await db_client.close()


app = FastAPI(lifespan=lifespan)
exception_handler(app)
