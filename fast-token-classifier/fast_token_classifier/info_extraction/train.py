from typing import Any

import click
from datasets import DatasetDict
from pydantic import BaseModel
from transformers import (
    AutoModelForTokenClassification,
    DataCollatorForTokenClassification,
    Trainer,
    TrainingArguments,
)
from typeguard import typechecked

from fast_token_classifier import get_rich_logger
from fast_token_classifier.config import config
from fast_token_classifier.info_extraction import (
    TOKENIZER,
    compute_metrics,
    ingest_data,
    login_into_hub,
    tokenize_and_align_labels,
)

logger = get_rich_logger()


class TrainTokenClassificationModel(BaseModel):
    # Constants
    ID_2_LABEL: dict[str, Any] = config.model_config_schema.ID_2_LABEL
    LABEL_2_ID: dict[str, Any] = config.model_config_schema.LABEL_2_ID
    PATH: str = config.model_config_schema.DATA_FILE_NAME
    MODEL_CHECKPOINT: str = config.model_config_schema.MODEL_CHECKPOINT
    OUTPUT_DIR: str = config.training_args_schema.OUTPUT_DIR
    STRATEGY: str = config.training_args_schema.STRATEGY
    LEARNING_RATE: float = config.training_args_schema.LEARNING_RATE
    NUM_EPOCHS: int = config.training_args_schema.NUM_EPOCHS
    WEIGHT_DECAY: float = config.training_args_schema.WEIGHT_DECAY

    @typechecked
    def _load_dataset(self) -> DatasetDict:
        """This loads the dataset"""
        raw_datasets: DatasetDict = ingest_data(path=self.PATH)
        return raw_datasets

    @typechecked
    def _tokenize_data(self) -> DatasetDict:
        try:
            raw_datasets = self._load_dataset()
            tokenized_datasets: DatasetDict = raw_datasets.map(
                tokenize_and_align_labels,
                batched=True,
                remove_columns=raw_datasets["train"].column_names,
            )
            logger.info("Dataset successfully tokenized!")
            return tokenized_datasets

        except Exception as err:
            logger.error(f"Error tokenizing the data! \n{err}")

    @typechecked
    def _prepare_model_for_training(self) -> Any:
        try:
            model = AutoModelForTokenClassification.from_pretrained(
                self.MODEL_CHECKPOINT,
                id2label=self.ID_2_LABEL,
                label2id=self.LABEL_2_ID,
            )
            logger.info("Transformer model successfully prepared!")
            return model

        except Exception as err:
            logger.error(f"Error preparing the transformer model! \n{err}")

    def train_model(self) -> None:
        """This is used to train the model."""
        model: AutoModelForTokenClassification = self._prepare_model_for_training()
        tokenized_dataset: DatasetDict = self._tokenize_data()
        data_collator: DataCollatorForTokenClassification = DataCollatorForTokenClassification(
            tokenizer=TOKENIZER
        )
        try:
            args: TrainingArguments = TrainingArguments(
                self.OUTPUT_DIR,
                evaluation_strategy=self.STRATEGY,
                save_strategy=self.STRATEGY,
                learning_rate=self.LEARNING_RATE,
                num_train_epochs=self.NUM_EPOCHS,
                weight_decay=self.WEIGHT_DECAY,
                push_to_hub=True,
            )
            trainer = Trainer(
                model=model,
                args=args,
                train_dataset=tokenized_dataset.get("train"),
                eval_dataset=tokenized_dataset.get("validation"),
                data_collator=data_collator,
                compute_metrics=compute_metrics,
                tokenizer=TOKENIZER,
            )
            logger.info("Successfully initialized trainer!")
            trainer.train()
            logger.info(">>>> Training successfully completed! <<<<")

        except Exception as err:
            logger.error(f"Error training the transformer model! \n{err}")


@click.command()
def train_model() -> None:
    """This trains the named entity recognition model."""
    login_into_hub()
    ner_model = TrainTokenClassificationModel()
    ner_model.train_model()
    click.secho(message=">>>> Training Done!!! <<<<", bold=True, bg="blue", fg="white")


if __name__ == "__main__":
    train_model()
