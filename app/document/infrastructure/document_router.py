import os
import shutil
from typing import Annotated

from fastapi import APIRouter, UploadFile, File, Body, status, Path, BackgroundTasks

from app.document.domain.document import Document
from app.document.infrastructure.di import (
    DocumentServiceDi,
    ChunkServiceDi,
)
from app.shared.domain.exceptions import IllegalArgumentException

router = APIRouter(prefix="/document", tags=["Document"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Document,
)
async def save(
    document: Annotated[Document, Body(...)],
    document_service: DocumentServiceDi,
):
    await document_service.save(document=document)
    return document


@router.post(
    "/{document_id}/embeddings",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
)
async def process_file(
    document_id: Annotated[str, Path(...)],
    file: Annotated[UploadFile, File(...)],
    document_service: DocumentServiceDi,
    chunk_service: ChunkServiceDi,
    background_tasks: BackgroundTasks,
):
    if file.content_type != "application/pdf" and not file.filename.endswith(".pdf"):
        raise IllegalArgumentException(
            message="Invalid file type. Only PDF files are allowed",
        )
    document = await document_service.find_one_by_id(document_id=document_id)

    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    file_path = os.path.join(temp_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    background_tasks.add_task(
        chunk_service.process_document,
        document=document,
        path=file_path,
    )
    return document_id
