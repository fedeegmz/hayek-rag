from abc import ABC, abstractmethod

from app.document.domain.chunk import Chunk


class ChunkRepository(ABC):
    @abstractmethod
    async def save(self, chunks: list[Chunk]) -> None:
        pass
