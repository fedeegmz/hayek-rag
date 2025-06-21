from typing import Annotated

from fastapi import Depends

from app.document.application.save_document import SaveDocument
from app.document.domain.document_repository import DocumentRepository
from app.document.domain.embedding_generator import EmbeddingGenerator
from app.document.domain.pdf_handler import PdfHandler
from app.document.infrastructure.embedding_generator_impl import EmbeddingGeneratorImpl
from app.document.infrastructure.mongodb_document_repository import (
    MongoDbDocumentRepository,
)
from app.document.infrastructure.pdf_hanlder_impl import PdfHandlerImpl
from app.shared.infrastructure.adapters.voyage_embedding_generator import (
    VoyageEmbeddingGenerator,
)
from app.shared.infrastructure.di.database import DbSession


def _get_repository(db_session: DbSession) -> DocumentRepository:
    return MongoDbDocumentRepository(db_session=db_session)


DocumentRepositoryDi = Annotated[DocumentRepository, Depends(_get_repository)]


def _get_embedding_generator() -> EmbeddingGenerator:
    return EmbeddingGeneratorImpl(VoyageEmbeddingGenerator())


EmbeddingGeneratorDi = Annotated[EmbeddingGenerator, Depends(_get_embedding_generator)]


def _get_pdf_handler() -> PdfHandler:
    return PdfHandlerImpl()


PdfHandlerDi = Annotated[PdfHandler, Depends(_get_pdf_handler)]


def _get_save_document_service(
    document_repository: DocumentRepositoryDi,
    embedding_generator: EmbeddingGeneratorDi,
    pdf_handler: PdfHandlerDi,
) -> SaveDocument:
    return SaveDocument(
        document_repository=document_repository,
        embedding_generator=embedding_generator,
        pdf_handler=pdf_handler,
    )


SaveDocumentDi = Annotated[SaveDocument, Depends(_get_save_document_service)]
