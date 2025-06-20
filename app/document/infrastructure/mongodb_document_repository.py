from typing import override

from pymongo.asynchronous.client_session import AsyncClientSession

from app.document.domain.document import Document
from app.document.domain.document_repository import DocumentRepository
from app.shared.domain.exceptions import NotFoundException


class MongoDbDocumentRepository(DocumentRepository):
    def __init__(self, db_session: AsyncClientSession):
        self.db_session = db_session
        self.collection = db_session.client.hayek.documents

    @override
    async def find_one_by_id(self, document_id: str) -> Document:
        document = await self.collection.find_one(
            filter={"id": document_id}, session=self.db_session
        )
        if document is not None:
            return Document(**document)
        raise NotFoundException(f"Document with id {document_id} not found")

    @override
    async def save(self, document: Document) -> None:
        document_dict = document.model_dump()
        await self.collection.replace_one(
            filter={"id": document.id},
            replacement=document_dict,
            session=self.db_session,
            upsert=True,
        )
