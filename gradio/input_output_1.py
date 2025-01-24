import gradio as gr
import cv2

# Text
# def greet(name):
#     return "Hello " + name + "!"

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# iface = gr.Interface(fn=greet, inputs=gr.Textbox(lines=5, placeholder="Enter your name", label="input: "), outputs=gr.Textbox(label="output: "))

# Image


def RGB2Gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray


iface = gr.Interface(fn=RGB2Gray, inputs="image", outputs=gr.Image())

# Audio
# def file_path(input):
#     return input
# iface = gr.Interface(fn=file_path, inputs=gr.Audio(sources='microphone', type='filepath'), outputs="text")

if __name__ == "__main__":
    iface.launch()
