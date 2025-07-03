from pymongo.asynchronous.client_session import AsyncClientSession

from app.core.settings import settings
from app.document.domain.chunk import Chunk
from app.document.domain.chunk_repository import ChunkRepository
from app.shared.domain.exceptions import NotSaveException


class MongoDBChunkRepository(ChunkRepository):
    def __init__(self, db_session: AsyncClientSession) -> None:
        self.db_session = db_session
        self.collection = db_session.client[settings.db_name].document_chunks

    async def save(self, chunks: list[Chunk]) -> None:
        result = await self.collection.insert_many(
            documents=[chunk.model_dump() for chunk in chunks],
            session=self.db_session,
        )
        if len(result.inserted_ids) < len(chunks):
            raise NotSaveException("All chunks were not saved")
