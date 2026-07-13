from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        answer=(
            f"Backend is working. You asked: '{request.message}'. "
            f"Your role is '{request.role}'. RAG will be added in a later phase."
        ),
        sources=[],
    )