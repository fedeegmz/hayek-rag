from app.document.domain.chunk import Chunk
from app.document.domain.chunk_repository import ChunkRepository
from app.document.domain.document import Document
from app.document.domain.embedding_generator import EmbeddingGenerator
from app.document.domain.pdf_handler import PdfHandler

MIN_WORDS_PER_PAGE = 20


class ChunkService:
    def __init__(
        self,
        chunk_repository: ChunkRepository,
        embedding_generator: EmbeddingGenerator,
        pdf_handler: PdfHandler,
    ) -> None:
        self.chunk_repository = chunk_repository
        self.embedding_generator = embedding_generator
        self.pdf_handler = pdf_handler

    async def process_document(self, document: Document, path: str) -> None:
        self.pdf_handler.set_path(path)
        total_pages = self.pdf_handler.get_page_count()
        index = 0
        chunks: list[Chunk] = []
        while index < total_pages:
            text = await self.pdf_handler.extract_text(index)
            data = text.split(" ")
            if len(data) > MIN_WORDS_PER_PAGE:
                # cleaned page
                # TODO: chunks
                embedding = await self.embedding_generator.generate(
                    [x for x in data if x]
                )
                chunk = Chunk(
                    document_id=document.id,
                    text=text,
                    embeddings=embedding,
                )
                chunks.append(chunk)
            index += 1
        await self.chunk_repository.save(chunks)
