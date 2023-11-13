from typing import Any, Optional

import numpy as np
from datasets import load_metric
from transformers import AutoTokenizer
from typeguard import typechecked

from fast_token_classifier import get_rich_logger
from fast_token_classifier.config import config

# from src.info_extraction import

logger = get_rich_logger()
model_checkpoint: str = config.model_config_schema.MODEL_CHECKPOINT
label_names: list[str] = config.model_config_schema.LABEL_NAMES


@typechecked
def load_tokenizer(model_checkpoint: str) -> Any:
    """This loads the Huggingface tokenizer."""
    try:
        tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        logger.info("Tokenizer successfully loaded!")
        return tokenizer

    except FileNotFoundError as err:
        logger.error(f"Error loading the tokenizer! {err}")


@typechecked
def align_labels_with_tokens(labels: list[int], word_ids: list[Optional[int]]) -> list[int]:
    """This ensures that the new labels aligns with the tokens.
    e.g.
    original tokens: [0, 1, 2, 3, 4]
    original labels: [3, 0, 0, 5, 0]

    aligned tokens: [None, 0, 1, 2, 3, 3, 4, None]
    aligned labels: [-100, 3, 0, 0, 5, 5, 0, -100]
    """
    new_labels: list[int] = []
    current_word: Optional[int] = None

    for word_id in word_ids:
        # If the current_word is not None
        if word_id != current_word:
            # If it's NOT a special token!
            current_word = word_id  # Update the current_word
            label: int = -100 if word_id is None else labels[word_id]
            new_labels.append(label)

        elif word_id is None:
            # Special token
            new_labels.append(-100)

        else:
            # Same word as previous token i.e. current_word == word_id
            label: int = labels[word_id]  # type: ignore[no-redef]
            # If the label is B-XXX we change it to I-XXX
            # i.e odd labels are B-XXX while even labels are I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)

    return new_labels


TOKENIZER: AutoTokenizer = load_tokenizer(model_checkpoint=model_checkpoint)


@typechecked
def tokenize_and_align_labels(examples: dict[str, Any]) -> dict[str, Any]:
    """This is used to tokenize and align the labels of the dataset."""
    tokenized_inputs: dict[str, Any] = TOKENIZER(
        examples["tokens"], truncation=True, is_split_into_words=True
    )
    all_labels: list[str] = examples["ner_tags"]
    new_labels: list[list[int]] = []
    for i, labels in enumerate(all_labels):
        word_ids = tokenized_inputs.word_ids(i)  # type: ignore[attr-defined]
        new_labels.append(align_labels_with_tokens(labels, word_ids))

    # Create a new label!
    tokenized_inputs["labels"] = new_labels
    return tokenized_inputs


@typechecked
def compute_metrics(eval_preds: tuple[Any, Any]) -> dict[str, Any]:
    """This is used to calculate the evaluation metrics."""
    metric = load_metric("seqeval")
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)

    # Remove ignored index (special tokens) and convert to labels
    true_labels = [[label_names[l] for l in label if l != -100] for label in labels]
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    all_metrics = metric.compute(predictions=true_predictions, references=true_labels)

    return {
        "precision": all_metrics["overall_precision"],
        "recall": all_metrics["overall_recall"],
        "f1": all_metrics["overall_f1"],
        "accuracy": all_metrics["overall_accuracy"],
    }
