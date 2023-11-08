import os
from typing import Optional

from dotenv import load_dotenv
from typeguard import typechecked

load_dotenv()


@typechecked
def authenticate() -> tuple[Optional[str], Optional[str], Optional[str]]:
    """This is used to load the credentials."""
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    return (HUGGINGFACE_TOKEN, USERNAME, PASSWORD)


(HUGGINGFACE_TOKEN, USERNAME, PASSWORD) = authenticate()
