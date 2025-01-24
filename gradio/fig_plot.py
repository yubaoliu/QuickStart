import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def fig_output(x):
    Fs = 8000
    f = 5
    sample = 10
    x=np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    plt.plot(x, y)
    return plt

demo = gr.Interface(fn=fig_output, inputs=None, outputs=gr.Plot())

if __name__ == "__main__": 
    demo.launch()