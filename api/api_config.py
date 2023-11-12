# type: ignore
import logging
import sys
from types import FrameType

from loguru import logger
from pydantic import AnyHttpUrl, BaseSettings

from api.core import config


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO


class Settings(BaseSettings):
    """These settings ca be overriden using environment variables."""

    API_VERSION_STR: str = config.api_config_schema.API_VERSION_STR
    API_FULL_VERSION: str = config.api_config_schema.API_FULL_VERSION
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    PROJECT_NAME: str = config.api_config_schema.PROJECT_NAME
    RELOAD: bool = False
    logging: LoggingSettings = LoggingSettings()

    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://localhost:3000",
        "https://localhost:8000",
    ]

    class Config:
        case_sensitive: bool = True
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"


# This is the config for handling the logs. (Copied)
# See: https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging  # noqa
class InterceptHandler(logging.Handler):
    """Configuration for the custom logger."""

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = tp.cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def setup_app_logging(config: Settings) -> None:
    """THis is used to prepare custom logging for the app."""

    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}])


# Create an instance
settings = Settings()
