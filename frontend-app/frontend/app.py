import os
from typing import Any

import gradio as gr
import requests  # type: ignore
from typeguard import typechecked

# Custom
from frontend import get_rich_logger
from frontend.config import config

logger = get_rich_logger()

API_VERSION_STR: str = config.fe_config_schema.API_VERSION_STR
HOST: str = config.fe_config_schema.HOST
PORT: int = config.fe_config_schema.PORT
GRADIO_PORT: int = config.fe_config_schema.GRADIO_PORT
PREFIX: str = config.fe_config_schema.PREFIX
url: str = f"http://{HOST}:{PORT}/{API_VERSION_STR}/{PREFIX}"

# Environment variable
URL: str = os.getenv("URL", url)


@typechecked
def translate(data: str) -> list[dict[str, Any]]:
    response = requests.post(URL, json={"data": data})
    result: list[dict[str, Any]] = response.json().get("result")
    logger.info(">>>> Request precessed! <<<<")
    logger.info(result)
    return result


with gr.Blocks() as demo:
    name = gr.Textbox(label="Text")
    output = gr.Textbox(label="Output")
    clf_btn = gr.Button("Classify")
    clf_btn.click(fn=translate, inputs=name, outputs=output, api_name="token_classifier")


if __name__ == "__main__":
    demo.launch(show_api=True, server_name=HOST, server_port=GRADIO_PORT)
