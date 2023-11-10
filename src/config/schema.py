"""
This module is used to validate the data.

author: Chinedu Ezeofor
"""

from typing import Any

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class APIConfigSchema(BaseModel):
    """API Configurations."""

    API_VERSION_STR: str
    API_FULL_VERSION: str
    PROJECT_NAME: str


class ModelConfigSchema(BaseModel):
    """All model variables."""

    DATA_FILE_NAME: str
    MODEL_CHECKPOINT: str
    AGGREGATION_STRATEGY: str
    TRAINED_MODEL_CHECKPOINT: str
    TASK: str
    LABEL_NAMES: list[str]
    LABEL_2_ID: dict[str, Any]
    ID_2_LABEL: dict[str, Any]


class TrainingArgsSchema(BaseModel):
    """Training Parameters."""

    OUTPUT_DIR: str
    STRATEGY: str
    MODEL_CHECKPOINT: str
    LEARNING_RATE: float
    NUM_EPOCHS: int
    WEIGHT_DECAY: float


class ConfigVars(BaseModel):
    """Main configuration object."""

    api_config_schema: APIConfigSchema
    model_config_schema: ModelConfigSchema
    training_args_schema: TrainingArgsSchema
