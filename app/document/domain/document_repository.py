from abc import ABC, abstractmethod

from app.document.domain.document import Document


class DocumentRepository(ABC):
    @abstractmethod
    async def find_one_by_id(self, document_id: str) -> Document:
        pass

    @abstractmethod
    async def save(self, document: Document) -> None:
        pass
