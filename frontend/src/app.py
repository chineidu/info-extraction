import gradio as gr


def greet(name: str) -> str:
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    name = gr.Textbox(label="Text")
    output = gr.Textbox(label="Output")
    greet_btn = gr.Button("Classify")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="token_classifier")


if __name__ == "__main__":
    demo.launch(show_api=True)
