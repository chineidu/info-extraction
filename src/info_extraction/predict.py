from typing import Any, TypeVar, Union

from transformers import pipeline
from typeguard import typechecked

from src import get_console_logger
from src.config import config

logger = get_console_logger()

AGGREGATION_STRATEGY: str = config.model_config_schema.AGGREGATION_STRATEGY
TASK: str = config.model_config_schema.TASK
TRAINED_MODEL_CHECKPOINT: str = config.model_config_schema.TRAINED_MODEL_CHECKPOINT
ModelInput: TypeVar = Union[str, list[str]]  # type: ignore[assignment]
Predictions: TypeVar = Union[list[dict[str, Any]], list[list[dict[str, Any]]]]  # type: ignore[assignment]


@typechecked
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
def predict(model_input: ModelInput) -> Predictions:  # type: ignore[valid-type]
    """This is used to make predictions using the NER language model."""
    token_classifier: pipeline = _load_model()
    logger.info("Making prediction ...")
    result: Predictions = token_classifier(model_input)  # type: ignore[valid-type]
    logger.info("Prediction successfully made!")
    return result


if __name__ == "__main__":
    from rich import print

    texts: list[str] = [
        "Mauricio Pochettino is the head coach of Chelsea FC.",
        "Olumo Rock is a landmark in Abeokuta, Nigeria.",
        "Lionel Messi won the latest edition of the FIFA World Cup in 2022.",
        """Solvify is a technology company that specializes in Internet-related
        services and products.""",
        "The Harry Potter series, authored by J.K. Rowling, remains a bestseller worldwide.",
        """On September 20, 2023, Apple unveiled its latest iPhone model at the tech conference
        in San Francisco.""",
    ]
    print(predict(texts))
