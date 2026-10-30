"""Application settings, loaded from environment / .env via pydantic-settings."""

from __future__ import annotations

from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables for libraries that read os.environ directly.

load_dotenv(override=False)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- credentials ---
    groq_api_key: str
    tavily_api_key: str | None = None

    # --- LangSmith observability ---
    langsmith_tracing: bool = False
    langsmith_api_key: str | None = None
    langsmith_project: str = "agentic-rag-assistant"
    langsmith_endpoint: str = "https://api.smith.langchain.com"

    # --- Models ---
    model_fast: str = "openai/gpt-oss-20b"
    model_heavy: str = "openai/gpt-oss-120b"

    # --- Local embeddings ---
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # --- Agent configuration ---
    reasoning_effort: str = "medium"

    # --- Storage / retrieval ---
    chroma_dir: str = "./chroma_db"
    chroma_collection: str = "documents"
    sqlite_path: str = "./memory.sqlite"
    retriever_k: int = 4
    sample_docs_dir: str = "./data/sample_docs"

    @property
    def web_backend(self) -> str:
        return "tavily" if self.tavily_api_key else "duckduckgo"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


settings = get_settings()
