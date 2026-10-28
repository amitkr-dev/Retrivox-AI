from rag_agent.main import get_app_info


def test_get_app_info():
    info = get_app_info()

    assert info["name"] == "Agentic RAG Assistant"
    assert info["version"] == "0.1.0"