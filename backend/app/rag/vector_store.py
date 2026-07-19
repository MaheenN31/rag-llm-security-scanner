from pathlib import Path
from typing import Any

import chromadb

from app.core.config import settings
from app.rag.embeddings import embed_texts
from app.rag.ingest import build_document_chunks


def get_chroma_client() -> chromadb.PersistentClient:
    db_path = Path(settings.chroma_db_dir)
    db_path.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(db_path))


def get_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(name=settings.chroma_collection_name)


def reset_collection():
    client = get_chroma_client()

    existing_collections = [collection.name for collection in client.list_collections()]

    if settings.chroma_collection_name in existing_collections:
        client.delete_collection(name=settings.chroma_collection_name)

    return client.get_or_create_collection(name=settings.chroma_collection_name)


def index_sample_documents() -> int:
    """
    Rebuild the Chroma collection from sample_docs.

    MVP behavior:
    - reset collection every time
    - load all chunks
    - embed chunks locally
    - store chunk metadata
    """
    collection = reset_collection()
    chunks = build_document_chunks(role=None)

    if not chunks:
        return 0

    ids = [chunk.chunk_id for chunk in chunks]
    documents = [chunk.content for chunk in chunks]
    embeddings = embed_texts(documents)

    metadatas: list[dict[str, Any]] = []

    for chunk in chunks:
        metadatas.append(
            {
                "chunk_id": chunk.chunk_id,
                "doc_id": chunk.doc_id,
                "document_title": chunk.document_title,
                "source": chunk.source,
                "classification": chunk.classification,
                "allowed_roles": ",".join(chunk.allowed_roles),
                "chunk_index": chunk.chunk_index,
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    return len(chunks)