from fastapi import APIRouter, Query

from app.models.schemas import (
    ChunkListResponse,
    DocumentDetail,
    DocumentListResponse,
)
from app.rag.ingest import (
    build_document_chunks,
    get_document_by_id,
    load_document_summaries,
)

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("", response_model=DocumentListResponse)
def list_documents():
    documents = load_document_summaries()

    return DocumentListResponse(
        documents=documents,
        count=len(documents),
    )


@router.get("/chunks", response_model=ChunkListResponse)
def list_chunks(role: str | None = Query(default=None)):
    chunks = build_document_chunks(role=role)

    return ChunkListResponse(
        chunks=chunks,
        count=len(chunks),
        role_filter=role,
    )


@router.get("/{doc_id}", response_model=DocumentDetail)
def read_document(doc_id: str):
    return get_document_by_id(doc_id)