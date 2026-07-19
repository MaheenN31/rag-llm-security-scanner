from typing import List


def split_text_into_chunks(
    text: str,
    chunk_size: int = 900,
    overlap: int = 120,
) -> List[str]:
    """
    Split text into readable chunks.

    This is a simple MVP chunker:
    - prefers paragraph boundaries
    - keeps chunks under the approximate chunk size
    - adds small overlap so context is not lost between chunks

    Later, we can replace this with token-aware chunking.
    """
    cleaned_text = text.strip()

    if not cleaned_text:
        return []

    paragraphs = [p.strip() for p in cleaned_text.split("\n\n") if p.strip()]

    chunks: List[str] = []
    current_parts: List[str] = []
    current_length = 0

    for paragraph in paragraphs:
        paragraph_length = len(paragraph)

        if current_parts and current_length + paragraph_length + 2 > chunk_size:
            chunk = "\n\n".join(current_parts).strip()
            chunks.append(chunk)

            if overlap > 0:
                overlap_text = chunk[-overlap:]
                current_parts = [overlap_text, paragraph]
                current_length = len(overlap_text) + paragraph_length
            else:
                current_parts = [paragraph]
                current_length = paragraph_length
        else:
            current_parts.append(paragraph)
            current_length += paragraph_length + 2

    if current_parts:
        chunks.append("\n\n".join(current_parts).strip())

    return chunks