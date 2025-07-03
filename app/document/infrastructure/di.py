from typing import Annotated

from fastapi import Depends

from app.document.application.chunk_service import ChunkService
from app.document.application.document_service import DocumentService
from app.document.domain.chunk_repository import ChunkRepository
from app.document.domain.document_repository import DocumentRepository
from app.document.domain.embedding_generator import EmbeddingGenerator
from app.document.domain.pdf_handler import PdfHandler
from app.document.infrastructure.embedding_generator_impl import EmbeddingGeneratorImpl
from app.document.infrastructure.mongodb_chunk_repository import MongoDBChunkRepository
from app.document.infrastructure.mongodb_document_repository import (
    MongoDbDocumentRepository,
)
from app.document.infrastructure.pdf_hanlder_impl import PdfHandlerImpl
from app.shared.infrastructure.adapters.voyage_embedding_generator import (
    VoyageEmbeddingGenerator,
)
from app.shared.infrastructure.di.database import DbSessionDi


def _get_chunk_repository(db_session: DbSessionDi) -> ChunkRepository:
    return MongoDBChunkRepository(db_session=db_session)


ChunkRepositoryDi = Annotated[ChunkRepository, Depends(_get_chunk_repository)]


def _get_embedding_generator() -> EmbeddingGenerator:
    return EmbeddingGeneratorImpl(VoyageEmbeddingGenerator())


EmbeddingGeneratorDi = Annotated[EmbeddingGenerator, Depends(_get_embedding_generator)]


def _get_pdf_handler() -> PdfHandler:
    return PdfHandlerImpl()


PdfHandlerDi = Annotated[PdfHandler, Depends(_get_pdf_handler)]


def _get_chunk_service(
    chunk_repository: ChunkRepositoryDi,
    embedding_generator: EmbeddingGeneratorDi,
    pdf_handler: PdfHandlerDi,
) -> ChunkService:
    return ChunkService(
        chunk_repository=chunk_repository,
        embedding_generator=embedding_generator,
        pdf_handler=pdf_handler,
    )


ChunkServiceDi = Annotated[ChunkService, Depends(_get_chunk_service)]


def _get_document_repository(db_session: DbSessionDi) -> DocumentRepository:
    return MongoDbDocumentRepository(db_session=db_session)


DocumentRepositoryDi = Annotated[DocumentRepository, Depends(_get_document_repository)]


def _get_document_service(
    document_repository: DocumentRepositoryDi,
) -> DocumentService:
    return DocumentService(document_repository=document_repository)


DocumentServiceDi = Annotated[DocumentService, Depends(_get_document_service)]
