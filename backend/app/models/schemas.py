from pydantic import BaseModel
from typing import List, Optional


class Source(BaseModel):
    document: str
    chunk_id: str


class ChatRequest(BaseModel):
    message: str
    role: str = "guest"


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source] = []


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str


class UploadResponse(BaseModel):
    filename: str
    status: str
    message: Optional[str] = None