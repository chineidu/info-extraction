"""
This module is used to validate the data.

author: Chinedu Ezeofor
"""

# Standard imports
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class ModelConfigSchema(BaseModel):
    """All model variables."""

    DATA_FILE_NAME: str
    MODEL_CHECKPOINT: str


class ConfigVars(BaseModel):
    """Main configuration object."""

    model_config_schema: ModelConfigSchema
    # path_config: PathConfig
