from abc import ABC, abstractmethod

from app.shared.domain.value_objects.embeddings import Embeddings


class VectorStore(ABC):
    @abstractmethod
    async def similarity_search(self, embeddings: Embeddings) -> Embeddings:
        pass
