from abc import ABC, abstractmethod


class LLM(ABC):
    @abstractmethod
    async def query(self, query: str | list[str]) -> str:
        pass
