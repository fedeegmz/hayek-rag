import os
import shutil

from fastapi import APIRouter, UploadFile, File, Body, status, Path

from app.document.domain.document import BaseDocument
from app.document.infrastructure.di import SaveDocumentDi
from app.shared.domain.exceptions import IllegalArgumentException

router = APIRouter(prefix="/document", tags=["Document"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=BaseDocument,
)
async def register_document(
    save_document_service: SaveDocumentDi,
    document: BaseDocument = Body(...),
):
    await save_document_service.register_document(document=document)
    return document


@router.post(
    "/{document_id}/embeddings",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
)
async def process_file(
    save_document_service: SaveDocumentDi,
    document_id: str = Path(...),
    file: UploadFile = File(...),
):
    if file.content_type != "application/pdf" and not file.filename.endswith(".pdf"):
        raise IllegalArgumentException(
            message="Invalid file type. Only PDF files are allowed"
        )

    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    file_path = os.path.join(temp_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # TODO: background task
    await save_document_service.process_embeddings(
        document_id=document_id, path=file_path
    )
    return document_id
