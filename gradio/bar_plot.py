import gradio as gr
import pandas as pd

simple = pd.DataFrame({'x': [1, 2, 3], 
                       'y': [4, 5, 6]})

demo = gr.Interface(fn=None, inputs=None, outputs=gr.BarPlot(simple, x="x", y="y"), title="Bar Plot Demo")

if __name__ == '__main__':
    demo.launch()