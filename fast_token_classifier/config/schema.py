"""
This module is used to validate the data.

author: Chinedu Ezeofor
"""

from typing import Any

from pydantic import BaseModel


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

    model_config_schema: ModelConfigSchema
    training_args_schema: TrainingArgsSchema
