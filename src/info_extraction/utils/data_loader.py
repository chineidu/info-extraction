from datasets import load_dataset
from datasets.dataset_dict import DatasetDict
from typeguard import typechecked

from src import get_console_logger

logger = get_console_logger()


@typechecked
def ingest_data(path: str = "conll2003") -> DatasetDict:
    """This is used to load the dataset from HugginFace Datasets."""

    loaded_datasets: DatasetDict = load_dataset(path=path)
    logger.info(f"Dataset with path: {path!r} has been loaded.")
    return loaded_datasets
