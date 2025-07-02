from abc import ABC, abstractmethod

from app.document.domain.document import Document
from app.shared.domain.value_objects.id import Id


class DocumentRepository(ABC):
    @abstractmethod
    async def find_one_by_id(self, document_id: Id) -> Document:
        pass

    @abstractmethod
    async def save(self, document: Document) -> None:
        pass
