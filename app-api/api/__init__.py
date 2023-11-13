import logging
from typing import Any, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rich.logging import RichHandler
from typeguard import typechecked

from api.api_config import settings  # type: ignore[attr-defined]
from api.v1.routes.health import root_router
from api.v1.routes.predict import pred_router


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"/{settings.API_VERSION_STR}/openapi.json",
        docs_url=f"/{settings.API_VERSION_STR}/docs",
        redoc_url=f"/{settings.API_VERSION_STR}/redoc",
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
    app.include_router(root_router)
    app.include_router(pred_router, prefix=f"/{settings.API_VERSION_STR}")
    return app
