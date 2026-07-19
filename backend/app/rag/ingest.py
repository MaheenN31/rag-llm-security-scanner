from pathlib import Path
from typing import List

import yaml
from fastapi import HTTPException

from app.core.config import settings
from app.models.schemas import (
    DocumentChunk,
    DocumentDetail,
    DocumentMetadata,
    DocumentSummary,
)
from app.rag.chunking import split_text_into_chunks


def _sample_docs_path() -> Path:
    return Path(settings.sample_docs_dir).resolve()


def _parse_markdown_with_front_matter(path: Path) -> tuple[DocumentMetadata, str]:
    raw_text = path.read_text(encoding="utf-8")

    if not raw_text.startswith("---"):
        raise ValueError(f"{path.name} is missing metadata front matter.")

    parts = raw_text.split("---", 2)

    if len(parts) < 3:
        raise ValueError(f"{path.name} has invalid metadata front matter.")

    metadata_raw = parts[1].strip()
    content = parts[2].strip()

    metadata_dict = yaml.safe_load(metadata_raw)

    if not isinstance(metadata_dict, dict):
        raise ValueError(f"{path.name} metadata is not valid YAML.")

    metadata = DocumentMetadata(
        doc_id=str(metadata_dict["doc_id"]),
        title=str(metadata_dict["title"]),
        owner=str(metadata_dict["owner"]),
        allowed_roles=list(metadata_dict["allowed_roles"]),
        classification=str(metadata_dict["classification"]),
        source=str(metadata_dict.get("source", path.name)),
    )

    return metadata, content


def load_document_details() -> List[DocumentDetail]:
    docs_dir = _sample_docs_path()

    if not docs_dir.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Sample documents directory not found: {docs_dir}",
        )

    documents: List[DocumentDetail] = []

    for path in sorted(docs_dir.glob("*.md")):
        metadata, content = _parse_markdown_with_front_matter(path)
        chunks = split_text_into_chunks(content)

        documents.append(
            DocumentDetail(
                **metadata.model_dump(),
                chunk_count=len(chunks),
                char_count=len(content),
                content=content,
            )
        )

    return documents


def load_document_summaries() -> List[DocumentSummary]:
    return [
        DocumentSummary(
            **document.model_dump(
                exclude={
                    "content",
                }
            )
        )
        for document in load_document_details()
    ]


def get_document_by_id(doc_id: str) -> DocumentDetail:
    for document in load_document_details():
        if document.doc_id == doc_id:
            return document

    raise HTTPException(
        status_code=404,
        detail=f"Document not found: {doc_id}",
    )


def build_document_chunks(role: str | None = None) -> List[DocumentChunk]:
    chunks: List[DocumentChunk] = []

    for document in load_document_details():
        if role and role not in document.allowed_roles:
            continue

        text_chunks = split_text_into_chunks(document.content)

        for index, content in enumerate(text_chunks, start=1):
            chunks.append(
                DocumentChunk(
                    chunk_id=f"{document.doc_id}_chunk_{index:03d}",
                    doc_id=document.doc_id,
                    document_title=document.title,
                    source=document.source,
                    classification=document.classification,
                    allowed_roles=document.allowed_roles,
                    chunk_index=index,
                    content=content,
                )
            )

    return chunks