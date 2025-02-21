import gradio as gr
from image_processor import process_image
from ai_handler import get_math_response

def main(image_sketchpad):
    image_description = None
    if image_sketchpad and image_sketchpad["composite"]:
        image_description = process_image(image_sketchpad["composite"])
    return get_math_response(image_description)

def build_ui():
    with gr.Blocks() as demo:
        gr.HTML(
            """<center><font size=5>✨<b>MathDoodle</b>✨</center>"""
            """\
<center><font size=3>This WebUI can converts handwritten math into accurate solutions using AI-powered recognition and preprocessing.</center>"""
            )
        with gr.Row():
            with gr.Column():
                input_sketchpad = gr.Sketchpad(type="pil", label="Sketch", layers=False, brush=gr.Brush())
                clear_btn = gr.ClearButton([input_sketchpad])
                submit_btn = gr.Button("Submit", variant="primary")
            with gr.Column():
                output_text = gr.Textbox(label="Output", interactive=False, lines=27)

        submit_btn.click(fn=main, inputs=[input_sketchpad], outputs=[output_text])
    return demo

demo = build_ui()
demo.launch()
