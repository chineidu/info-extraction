from typing import Any

import uvicorn
from fastapi import FastAPI

from src.api import create_app
from src.api.config import settings  # type: ignore[attr-defined]

app: FastAPI = create_app()


@app.get("/")
async def index() -> dict[str, Any]:
    return {
        "message": f"{settings.PROJECT_NAME!r} app is working",
        "status": "success!",
    }


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
