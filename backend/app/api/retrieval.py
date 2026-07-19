from fastapi import APIRouter, Query

from app.core.config import settings
from app.models.schemas import IndexResponse, RetrievalSearchResponse
from app.rag.retriever import search_relevant_chunks
from app.rag.vector_store import index_sample_documents

router = APIRouter(prefix="/retrieval", tags=["retrieval"])


@router.post("/index", response_model=IndexResponse)
def index_documents():
    indexed_count = index_sample_documents()

    return IndexResponse(
        status="indexed",
        indexed_chunks=indexed_count,
        collection_name=settings.chroma_collection_name,
    )


@router.get("/search", response_model=RetrievalSearchResponse)
def search_documents(
    query: str = Query(..., min_length=1),
    role: str = Query(default="guest"),
    top_k: int = Query(default=4, ge=1, le=10),
):
    results = search_relevant_chunks(
        query=query,
        role=role,
        top_k=top_k,
    )

    return RetrievalSearchResponse(
        query=query,
        role=role,
        results=results,
        count=len(results),
    )