import gradio as gr


def show_json():
    json_sample = {"name": "John", "age": 30, "city": "New York"}
    return json_sample

demo = gr.Interface(fn=show_json, inputs=None, outputs='json') 

if __name__ == "__main__":
    demo.launch()