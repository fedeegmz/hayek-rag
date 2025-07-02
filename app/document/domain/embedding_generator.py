from abc import ABC, abstractmethod

from app.shared.domain.value_objects.embeddings import Embeddings


class EmbeddingGenerator(ABC):
    @abstractmethod
    async def generate(self, data: list[str]) -> Embeddings:
        pass
