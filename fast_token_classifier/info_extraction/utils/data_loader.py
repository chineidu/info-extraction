from datasets import DatasetDict, load_dataset
from huggingface_hub import login
from typeguard import typechecked

from fast_token_classifier import get_rich_logger
from fast_token_classifier.creds import HUGGINGFACE_TOKEN

logger = get_rich_logger()
# Load environment variables


@typechecked
def ingest_data(path) -> DatasetDict:
    """This is used to load the dataset from HuggingFace Datasets."""
    try:
        loaded_datasets: DatasetDict = load_dataset(path=path)
        logger.info(f"Dataset with path: {path!r} has been loaded.")
        return loaded_datasets

    except ValueError as err:
        logger.error(err)


@typechecked
def login_into_hub() -> None:
    """This is used to login into HuggingFace Hub."""
    try:
        login(token=HUGGINGFACE_TOKEN, add_to_git_credential=True)
        logger.info(">>>> Login into HuggingFace Hub successful! <<<<")

    except ValueError as err:
        logger.error(err)
