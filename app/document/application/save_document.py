from app.document.domain.document import Document, BaseDocument
from app.document.domain.document_repository import DocumentRepository
from app.document.domain.embedding_generator import EmbeddingGenerator
from app.document.domain.pdf_handler import PdfHandler

MIN_WORDS_PER_PAGE = 20


class SaveDocument:
    def __init__(
        self,
        document_repository: DocumentRepository,
        embedding_generator: EmbeddingGenerator,
        pdf_handler: PdfHandler,
    ) -> None:
        self.document_repository = document_repository
        self.embedding_generator = embedding_generator
        self.pdf_handler = pdf_handler

    async def register_document(self, document: BaseDocument) -> None:
        full_document = Document(**document.model_dump())
        await self.document_repository.save(full_document)

    async def process_embeddings(self, document_id: str, path: str) -> None:
        # TODO: generate metadata
        self.pdf_handler.set_path(path)
        cleaned_pages = await self._get_cleaned_pages()
        document = await self.document_repository.find_one_by_id(document_id)
        chunks = self._generate_chunks(cleaned_pages)

        embeddings = await self.embedding_generator.generate(chunks)
        document.embeddings = embeddings
        await self.document_repository.save(document)

    async def _get_cleaned_pages(self) -> list[str]:
        total_pages = self.pdf_handler.get_page_count()
        index = 0
        cleaned_pages: list[str] = []
        while index < total_pages:
            text = await self.pdf_handler.extract_text(index)
            if len(text.split(" ")) > MIN_WORDS_PER_PAGE:
                cleaned_pages.append(text)
            index += 1
        return cleaned_pages

    @staticmethod
    def _generate_chunks(data: list[str]) -> list[str]:
        # TODO: implement
        return data
