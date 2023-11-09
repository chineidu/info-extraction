import os
import shutil

from typeguard import typechecked

from src import get_console_logger
from src.config import config

logger = get_console_logger()

DIRECTORY_PATHS: list[str] = [config.training_args_schema.OUTPUT_DIR]


@typechecked
def _create_dir(*, directory_path: str) -> None:
    """This is used to create a directory."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        logger.info(f"Directory path {directory_path!r} successfully created!")


@typechecked
def delete_dir(directory_path) -> None:
    """This is used to delete a directory."""
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        logger.warning(f"Directory path {directory_path!r} successfully deleted!")


@typechecked
def create_drectories() -> None:
    """This is used to create directories."""
    for path in DIRECTORY_PATHS:
        _create_dir(directory_path=path)


@typechecked
def delete_drectories() -> None:
    """This is used to delete directories."""
    for path in DIRECTORY_PATHS:
        delete_dir(directory_path=path)


if __name__ == "__main__":
    delete_drectories()
    create_drectories()