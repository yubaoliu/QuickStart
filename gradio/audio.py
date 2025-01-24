import gradio as gr

# method 1:
# def audio_fn(audio):
#     hz = audio[0]
#     data = audio[1]
#     return hz, data

# iface = gr.Interface(fn=audio_fn, inputs=gr.Audio(type="numpy"), outputs="audio")


# method 1: use filepath
def audio_fn(audio):
    return audio
iface = gr.Interface(fn=audio_fn, inputs=gr.Audio(type="filepath"), outputs="audio")

if __name__ == "__main__":   
    iface.launch()