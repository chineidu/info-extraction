from typing import Any

import gradio as gr
import requests  # type: ignore

from src.config import config

API_VERSION_STR: str = config.fe_config_schema.API_VERSION_STR
HOST: str = config.fe_config_schema.HOST
PORT: int = config.fe_config_schema.PORT
PREFIX: str = config.fe_config_schema.PREFIX
URL: str = f"http://{HOST}:{PORT}/{API_VERSION_STR}/{PREFIX}"


def translate(data: str) -> dict[str, Any]:
    response = requests.post(URL, json={"data": data})
    result: dict[str, Any] = response.json().get("result")
    return result


with gr.Blocks() as demo:
    name = gr.Textbox(label="Text")
    output = gr.Textbox(label="Output")
    clf_btn = gr.Button("Classify")
    clf_btn.click(fn=translate, inputs=name, outputs=output, api_name="token_classifier")


if __name__ == "__main__":
    demo.launch(show_api=True)
