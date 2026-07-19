from pydantic import BaseModel, Field
from typing import List, Optional


class Source(BaseModel):
    document: str
    chunk_id: str


class ChatRequest(BaseModel):
    message: str
    role: str = "guest"


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source] = Field(default_factory=list)


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str


class UploadResponse(BaseModel):
    filename: str
    status: str
    message: Optional[str] = None


class DocumentMetadata(BaseModel):
    doc_id: str
    title: str
    owner: str
    allowed_roles: List[str]
    classification: str
    source: str


class DocumentSummary(DocumentMetadata):
    chunk_count: int
    char_count: int


class DocumentDetail(DocumentSummary):
    content: str


class DocumentChunk(BaseModel):
    chunk_id: str
    doc_id: str
    document_title: str
    source: str
    classification: str
    allowed_roles: List[str]
    chunk_index: int
    content: str


class DocumentListResponse(BaseModel):
    documents: List[DocumentSummary]
    count: int


class ChunkListResponse(BaseModel):
    chunks: List[DocumentChunk]
    count: int
    role_filter: Optional[str] = None

class IndexResponse(BaseModel):
    status: str
    indexed_chunks: int
    collection_name: str


class RetrievalResult(BaseModel):
    chunk_id: str
    doc_id: str
    document_title: str
    source: str
    classification: str
    allowed_roles: List[str]
    content: str
    distance: float | None = None


class RetrievalSearchResponse(BaseModel):
    query: str
    role: str
    results: List[RetrievalResult]
    count: int