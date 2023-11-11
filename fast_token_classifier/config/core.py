from functools import lru_cache
from pathlib import Path
from typing import Any, Optional, Union

import yaml
from typeguard import typechecked

# Custom Imports
import fast_token_classifier
from fast_token_classifier import get_rich_logger
from fast_token_classifier.config.schema import (
    APIConfigSchema,
    ConfigVars,
    ModelConfigSchema,
    TrainingArgsSchema,
)

logger = get_rich_logger()
SRC_ROOT: Path = Path(fast_token_classifier.__file__).absolute().parent  # src/
ROOT: Path = SRC_ROOT.parent  # proj/src
CONFIG_FILEPATH: Path = SRC_ROOT / "config/config.yaml"
ENV_CONFIG_FILEPATH: Path = ROOT / ".env"
DATA_FILEPATH: Path = ROOT / "data"


@typechecked
@lru_cache(maxsize=None)
def load_yaml_file(*, filename: Optional[Path] = None) -> Union[dict[str, Any], None]:
    """This loads the YAML file as a dict."""
    if filename is None:
        filename = CONFIG_FILEPATH

    try:
        with open(filename, "r") as file:
            config_dict = yaml.safe_load(stream=file)
            logger.info("Config file successfully loaded!")
            return config_dict

    except FileNotFoundError as err:
        logger.error(f"No config file found! {err}")
        return None


@typechecked
def validate_config_file(*, filename: Optional[Path] = None) -> ConfigVars:
    """This loads the config as a Pydantic object."""
    config_dict = load_yaml_file(filename=filename)

    # Validate config
    config_file = ConfigVars(
        api_config_schema=APIConfigSchema(**config_dict),
        model_config_schema=ModelConfigSchema(**config_dict),
        training_args_schema=TrainingArgsSchema(**config_dict),
    )
    return config_file


config: ConfigVars = validate_config_file(filename=None)
