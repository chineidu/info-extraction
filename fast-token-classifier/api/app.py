import uvicorn
from fastapi import FastAPI

from api import create_app, settings

app: FastAPI = create_app()


def main() -> None:
    """This is the entrypoint."""

    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )


# if __name__ == "__main__":
# main()

# CLI
# uvicorn api.app:app --port 8008 --host "0.0.0.0"
