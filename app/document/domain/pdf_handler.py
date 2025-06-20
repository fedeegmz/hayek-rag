from abc import ABC, abstractmethod


class PdfHandler(ABC):
    @abstractmethod
    def set_path(self, path: str) -> None:
        pass

    @abstractmethod
    def get_page_count(self) -> int:
        pass

    @abstractmethod
    async def extract_text(self, page: int) -> str:
        pass
