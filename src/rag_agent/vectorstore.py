"""Chroma vector store, persisted to disk for zero-setup RAG."""

from __future__ import annotations

from functools import lru_cache

from langchain_chroma import Chroma

from rag_agent.config import settings
from rag_agent.embeddings import get_embeddings


@lru_cache(maxsize=1)
def get_vectorstore() -> Chroma:
    """Initialize and cache the persistent ChromaDB vector store."""
    return Chroma(
        collection_name=settings.chroma_collection,
        embedding_function=get_embeddings(),
        persist_directory=str(settings.chroma_dir),
    )


def collection_count() -> int:
    """Return the number of stored document chunks."""
    return get_vectorstore()._collection.count()