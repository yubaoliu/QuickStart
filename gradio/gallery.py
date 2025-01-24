import gradio as gr

def process():
    images = [
        "./images/266.jpg",
        "./images/267.jpg",
        "./images/268.jpg",
        "./images/269.jpg",
        "./images/270.jpg",
        "./images/271.jpg",
        "./images/272.jpg",
    ]
    return images

iface = gr.Interface(process, inputs=None, outputs=gr.Gallery(columns=3),
                     live=True)

if __name__ == "__main__":  
    iface.launch()