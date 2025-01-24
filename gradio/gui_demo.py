import gradio as gr


with gr.Blocks() as demo:
    with gr.Tab(label="txt2img"):
        with gr.Row():
            with gr.Column(scale=15):
                text1 = gr.Textbox(label="")
                text2 = gr.Textbox(label="")
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value="1")
                button2 = gr.Button(value="2")
                button3 = gr.Button(value="3")
                button4 = gr.Button(value="4")
            with gr.Column(scale=6):
                generate_button = gr.Button(
                    value="Generate", variant="primary", scale=1)
                with gr.Row():
                    dropdown1 = gr.Dropdown(
                        choices=["1", "2", "3", "4"], label="Style1")
                    dropdown2 = gr.Dropdown(
                        choices=["1", "2", "3", "4"], label="Style2")
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    dropdown3 = gr.Dropdown(
                        choices=["1", "2", "3", "4"], label="Sampling method")
                    slider1 = gr.Slider(
                        minimum=1, maximum=100, label="Sampling rate")
                checkboxgroup = gr.CheckboxGroup(
                    choices=["Restore faces", "Tiling", "Hires.fix"], label="")
                with gr.Row():
                    slider2 = gr.Slider(minimum=1, maximum=100, label="Width")
                    slider3 = gr.Slider(
                        minimum=1, maximum=100, label="Batch count")
                with gr.Row():
                    slider4 = gr.Slider(minimum=1, maximum=100, label="Height")
                    slider5 = gr.Slider(
                        minimum=1, maximum=100, label="Batch size")
                slider6 = gr.Slider(minimum=1, maximum=100, label="CFG scale")
                with gr.Row():
                    number1 = gr.Number(label="Seed", scale=6)
                    button5 = gr.Button(value="Randomize", min_width=1)
                    button6 = gr.Button(value="Reset", min_width=1)
                    checkbox1 = gr.Checkbox(label="Extra", min_width=10)
                dropdown4 = gr.Dropdown(
                    choices=["1", "2", "3", "4"], label="Script")
            with gr.Column():
                gallery = gr.Gallery(["./images/266.jpg",
                                      "./images/267.jpg",
                                      "./images/268.jpg",
                                      "./images/269.jpg",
                                      "./images/270.jpg",
                                      "./images/271.jpg",
                                      "./images/272.jpg",], columns=3)
                with gr.Row():
                    button7 = gr.Button(value="Save", min_width=1)
                    button8 = gr.Button(value="Load", min_width=1)
                    button9 = gr.Button(value="zip", min_width=1)
                    button10 = gr.Button(value="send to img2img", min_width=1)
                    button11 = gr.Button(value="Send to inpaint", min_width=1)
                    button12 = gr.Button(value="Send to extras", min_width=1)

                txt3 = gr.Textbox(lines=10, label="Output")
demo.launch()
