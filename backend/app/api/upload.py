from fastapi import APIRouter, UploadFile, File
from app.models.schemas import UploadResponse

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    return UploadResponse(
        filename=file.filename or "unknown",
        status="received",
        message="Upload endpoint is working. Document ingestion will be added later.",
    )