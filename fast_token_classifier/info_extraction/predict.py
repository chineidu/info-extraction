from functools import lru_cache
from typing import Any, TypeAlias, Union

from transformers import pipeline
from typeguard import typechecked

from fast_token_classifier import get_rich_logger
from fast_token_classifier.config import config

logger = get_rich_logger()

AGGREGATION_STRATEGY: str = config.model_config_schema.AGGREGATION_STRATEGY
TASK: str = config.model_config_schema.TASK
TRAINED_MODEL_CHECKPOINT: str = config.model_config_schema.TRAINED_MODEL_CHECKPOINT
ModelInput: TypeAlias = Union[str, list[str]]
Predictions: TypeAlias = Union[list[dict[str, Any]], list[list[dict[str, Any]]]]


@typechecked
@lru_cache(maxsize=None)
def _load_model() -> Any:
    """This is used to load the NER language model."""
    NER_model: pipeline = pipeline(
        task=TASK,
        model=TRAINED_MODEL_CHECKPOINT,
        aggregation_strategy=AGGREGATION_STRATEGY,
    )
    logger.info("Model successfully loaded!")
    return NER_model


@typechecked
@lru_cache(maxsize=None)
def classify_tokens(*, model_input: ModelInput) -> Predictions:
    """This is used to make predictions using the NER language model."""
    token_classifier: pipeline = _load_model()
    logger.info(" >>>> Making prediction <<<<")
    result: Predictions = token_classifier(model_input)
    logger.info("Prediction successfully made!")
    return result


@typechecked
def json_format_response(input_value: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """This is used to convert the NumPy values to stings."""
    return [{k: str(v) for k, v in row.items()} for row in input_value]


if __name__ == "__main__":
    import json

    import numpy as np
    from rich import print

    text: str = "Elon Musk is the CEO of X, Tesla, SpaceX, and other companies."
    texts: list[str] = [
        "Mauricio Pochettino is the head coach of Chelsea FC.",
        "Olumo Rock is a landmark in Abeokuta, Nigeria.",
        "Lionel Messi won the latest edition of the FIFA World Cup in 2022.",
        (
            "Solvify is a technology company that specializes in Internet-related"
            + "services and products."
        ),
        "The Harry Potter series, authored by J.K. Rowling, remains a bestseller worldwide.",
        (
            "On September 20, 2023, Apple unveiled its latest iPhone model at the tech"
            + "conference in San Francisco."
        ),
    ]
    # result = classify_tokens(model_input=text)
    # print(result)
