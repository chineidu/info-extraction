from pathlib import Path
from typing import Any, Optional, Union

import yaml
from typeguard import typechecked

# Custom Imports
import api
from api.logger import get_rich_logger
from api.v1.schemas.api_schema import APIConfigSchema, ConfigVars

SRC_ROOT: Path = Path(api.__file__).absolute().parent  # src/
ROOT: Path = SRC_ROOT.parent  # proj/src
CONFIG_FILEPATH: Path = SRC_ROOT / "api_config.yaml"


logger = get_rich_logger()


@typechecked
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
    config_file = ConfigVars(api_config_schema=APIConfigSchema(**config_dict))
    return config_file


config: ConfigVars = validate_config_file(filename=None)
