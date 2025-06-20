from abc import ABC, abstractmethod


class EmbeddingGenerator(ABC):
    @abstractmethod
    async def generate(self, data: list[str]) -> list[list[int | float]]:
        pass
