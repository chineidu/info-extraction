import uvicorn
from fastapi import FastAPI

from src.api import create_app
from src.api.config import settings  # type: ignore[attr-defined]

app: FastAPI = create_app()


def main() -> None:
    """This is the entrypoint."""
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )


if __name__ == "__main__":
    main()
