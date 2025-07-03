from typing import override

from pymongo.asynchronous.client_session import AsyncClientSession

from app.core.settings import settings
from app.document.domain.document import Document
from app.document.domain.document_repository import DocumentRepository
from app.shared.domain.exceptions import NotFoundException, NotSaveException


class MongoDbDocumentRepository(DocumentRepository):
    def __init__(self, db_session: AsyncClientSession) -> None:
        self.db_session = db_session
        self.collection = db_session.client[settings.db_name].documents

    @override
    async def find_one_by_id(self, document_id: str) -> Document:
        document = await self.collection.find_one(
            filter={"id": document_id},
            session=self.db_session,
        )
        if document is not None:
            return Document(**document)
        raise NotFoundException(f"Document with id {document_id} not found")

    @override
    async def save(self, document: Document) -> None:
        try:
            await self.find_one_by_id(document.id)
            raise NotSaveException(f'Document "{document.title}" already exists')
        except NotFoundException:
            await self.collection.insert_one(
                document=document.model_dump(),
                session=self.db_session,
            )
