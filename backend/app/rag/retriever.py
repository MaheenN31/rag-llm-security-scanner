from typing import Any, List

from app.models.schemas import RetrievalResult
from app.rag.embeddings import embed_query
from app.rag.vector_store import get_collection


def _metadata_roles(metadata: dict[str, Any]) -> list[str]:
    raw_roles = metadata.get("allowed_roles", "")

    if not isinstance(raw_roles, str):
        return []

    return [role.strip() for role in raw_roles.split(",") if role.strip()]


def search_relevant_chunks(
    query: str,
    role: str,
    top_k: int = 4,
) -> List[RetrievalResult]:
    """
    Search ChromaDB and enforce role filtering after retrieval.

    MVP approach:
    - ask Chroma for more than top_k
    - filter unauthorized chunks in Python
    - return only chunks where role is in allowed_roles

    Later, we can optimize metadata filtering.
    """
    collection = get_collection()
    query_embedding = embed_query(query)

    result_limit = max(top_k * 4, 10)

    raw_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=result_limit,
        include=["documents", "metadatas", "distances"],
    )

    documents = raw_results.get("documents", [[]])[0]
    metadatas = raw_results.get("metadatas", [[]])[0]
    distances = raw_results.get("distances", [[]])[0]

    results: List[RetrievalResult] = []

    for document, metadata, distance in zip(documents, metadatas, distances):
        if metadata is None:
            continue

        allowed_roles = _metadata_roles(metadata)

        if role not in allowed_roles:
            continue

        results.append(
            RetrievalResult(
                chunk_id=str(metadata.get("chunk_id", "")),
                doc_id=str(metadata.get("doc_id", "")),
                document_title=str(metadata.get("document_title", "")),
                source=str(metadata.get("source", "")),
                classification=str(metadata.get("classification", "")),
                allowed_roles=allowed_roles,
                content=document,
                distance=float(distance) if distance is not None else None,
            )
        )

        if len(results) >= top_k:
            break

    return results