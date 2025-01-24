import gradio as gr
import cv2

input_list = [ 
              gr.Audio(sources=["microphone", "upload"], type="filepath", label="Audio"),
              gr.Checkbox(label="Checkbox"),
              gr.ColorPicker(label="Color Picker"),
              gr.DataFrame(label="Dataframe"),
              gr.Dropdown(choices=["Option 1", "Option 2", "Option 3"], label="Dropdown"),
              gr.File(type="binary", label="File"),
              gr.Image(sources=["webcam", "upload"], label="Image"),
              gr.Number(label="Number"),
              gr.Radio(choices=["Option 1", "Option 2", "Option 3"], label="Radio"),
              gr.Slider(label="Slider"),
              gr.Textbox(label="Textbox"),
              gr.Video(sources=["webcam", "upload"], label="Video"),
              gr.TextArea(label="TextArea"),
]

output_list = [
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
             gr.Textbox(label="Output Textbox"),
]

def input_and_output(*intput_data):
    return intput_data


iface = gr.Interface(fn=input_and_output, 
                     inputs=input_list,
                     outputs=output_list, 
                     title="Input and Output Example",
                     live=True)
iface.launch()