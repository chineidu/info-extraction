from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.config import settings  # type: ignore[attr-defined]


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_VERSION_STR}/openapi.json",
        docs_url=f"{settings.API_VERSION_STR}/docs",
        redoc_url=f"{settings.API_VERSION_STR}/redoc",
    )
    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Add routers
    # app.include_router(root_router, prefix="/")
    return app
