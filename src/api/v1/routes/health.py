from typing import Any

from fastapi import APIRouter

from src.api.config import settings  # type: ignore[attr-defined]
from src.api.v1.schemas import IndexSchema

root_router: APIRouter = APIRouter()


@root_router.get(
    "/health",
    response_model=IndexSchema,
)
async def index() -> dict[str, Any]:
    """This is the index of the api."""
    return {
        "message": f"{settings.PROJECT_NAME!r} app is working",
        "status": "success!",
    }
