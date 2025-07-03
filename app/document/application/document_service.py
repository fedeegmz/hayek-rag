from app.document.domain.document import Document
from app.document.domain.document_repository import DocumentRepository
from app.shared.domain.value_objects.id import Id


class DocumentService:
    def __init__(self, document_repository: DocumentRepository) -> None:
        self.document_repository = document_repository

    async def find_one_by_id(self, document_id: Id) -> Document:
        return await self.document_repository.find_one_by_id(document_id)

    async def save(self, document: Document) -> None:
        await self.document_repository.save(document)
