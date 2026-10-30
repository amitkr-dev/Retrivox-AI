"""Groq chat model factories."""

from __future__ import annotations

from langchain_groq import ChatGroq

from rag_agent.config import settings


def fast_model() -> ChatGroq:
    """Small, fast model for routine agent operations."""
    return ChatGroq(
        model=settings.model_fast,
        api_key=settings.groq_api_key,
        temperature=0,
        streaming=True,
    )


def heavy_model() -> ChatGroq:
    """Reasoning model for planning and answer synthesis."""
    return ChatGroq(
        model=settings.model_heavy,
        api_key=settings.groq_api_key,
        temperature=0,
        streaming=True,
        reasoning_effort=settings.reasoning_effort,
    )
