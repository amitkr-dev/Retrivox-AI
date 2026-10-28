from rag_agent.config import PROJECT_NAME, VERSION


def get_app_info() -> dict[str, str]:
    """Return basic application information."""
    return {
        "name": PROJECT_NAME,
        "version": VERSION,
    }


if __name__ == "__main__":
    print(get_app_info())