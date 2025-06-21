from typing import override

from pypdf import PdfReader

from app.document.domain.pdf_handler import PdfHandler
from app.shared.domain.exceptions import UninitializedException


class PdfHandlerImpl(PdfHandler):
    def __init__(self) -> None:
        self.reader: PdfReader | None = None

    @override
    def set_path(self, path: str) -> None:
        self.reader = PdfReader(path)

    @override
    def get_page_count(self) -> int:
        if self.reader is not None:
            return len(self.reader.pages)
        raise UninitializedException("PdfHandler is not initialized")

    @override
    async def extract_text(self, page: int) -> str:
        if self.reader is not None:
            return self.reader.pages[page].extract_text()
        raise UninitializedException("PdfHandler is not initialized")
