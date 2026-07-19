from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv
import os

PROJECT_ROOT = Path(__file__).resolve().parents[3]

load_dotenv(PROJECT_ROOT / ".env")


class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "RAG LLM Security Scanner")
    app_env: str = os.getenv("APP_ENV", "development")
    backend_host: str = os.getenv("BACKEND_HOST", "127.0.0.1")
    backend_port: int = int(os.getenv("BACKEND_PORT", "8000"))

    sample_docs_dir: str = os.getenv(
        "SAMPLE_DOCS_DIR",
        str(PROJECT_ROOT / "sample_docs"),
    )

    chroma_db_dir: str = os.getenv(
        "CHROMA_DB_DIR",
        str(PROJECT_ROOT / "chroma_db"),
    )

    chroma_collection_name: str = os.getenv(
        "CHROMA_COLLECTION_NAME",
        "rag_security_docs",
    )

    embedding_model_name: str = os.getenv(
        "EMBEDDING_MODEL_NAME",
        "sentence-transformers/all-MiniLM-L6-v2",
    )


settings = Settings()