import gradio as gr
from ultralytics import YOLO
from PIL import Image
import torch
import cv2
from torchvision import transforms

model_seg = YOLO('/home/qingbao/Data/Models/yolo/yolo11s.pt')
model_detect = YOLO('/home/qingbao/Data/Models/yolo/yolo11n-seg.pt')
model_cls = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18',
                           pretrained=True).eval()  # or yolov5n - yolov5x6, custom


file_path = './coco_labels.txt'
with open(file_path, 'r') as f:
    labels = f.readlines()
labels = [label.rstrip() for label in labels]


def segment(img):
    results = model_seg(img)
    for r in results:
        im_array = r.plot()
        img = Image.fromarray(im_array[..., ::-1])
    return img


def detect(img):
    results = model_detect(img)
    for r in results:
        im_array = r.plot()
        img = Image.fromarray(im_array[..., ::-1])
    return img


def classify(img):
    image = transforms.ToTensor()(img).unsqueeze(0)
    with torch.no_grad():
        predictions = torch.nn.functional.softmax(model_cls(image)[0], dim=0)
        confidences = {labels[i]: float(predictions[i])
                       for i in range(len(labels))}
    return confidences


with gr.Blocks() as demo:
    with gr.Tab("Classification"):
        gr.Markdown("## Classify an Image")
        with gr.Row():
            input_img = gr.Image(
                sources=["upload"], type="pil", label="Upload an Image")
            output_label = gr.Label(
                num_top_classes=10, label="Top 10 Classifications")
        gr.Examples([
            './images/sheep.jpg',
            './images/cat.jpg',
            './images/kids.jpg',
        ], inputs=[input_img])
        button = gr.Button("Classify", variant="primary")
        button.click(classify, inputs=input_img, outputs=output_label)

    with gr.Tab("Segmentation"):
        gr.Markdown("## Segment an Image")
        with gr.Row():
            input_img = gr.Image(
                sources=["upload"], type="pil", label="Upload an Image")
            output_img = gr.Image(type="pil", label="Segmented Image")
        gr.Examples([
            './images/sheep.jpg',
            './images/cat.jpg',
            './images/kids.jpg',
        ], inputs=[input_img])
        button = gr.Button("Segment", variant="primary")
        button.click(segment, inputs=input_img, outputs=output_img)

    with gr.Tab("Detection"):
        gr.Markdown("## Detect Objects in an Image")
        with gr.Row():
            input_img = gr.Image(
                sources=["upload"], type="pil", label="Upload an Image")
            output_img = gr.Image(type="pil", label="Detected Objects")
        gr.Examples([
            './images/sheep.jpg',
            './images/cat.jpg',
            './images/kids.jpg',
        ], inputs=[input_img])
        button = gr.Button("Detect", variant="primary")
        button.click(detect, inputs=input_img, outputs=output_img)

if __name__ == '__main__':
    demo.launch()
