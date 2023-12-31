from typing import Any

from fastapi import APIRouter

from api.api_config import settings  # type: ignore[attr-defined]
from api.v1.schemas import IndexSchema

root_router: APIRouter = APIRouter()


@root_router.get(
    "/health",
    response_model=IndexSchema,
)
async def index() -> dict[str, Any]:
    """This is the index of the api."""
    return {
        "message": f"{settings.PROJECT_NAME} app is working !!!",
        "version": settings.API_FULL_VERSION,
        "status": "success!",
    }
