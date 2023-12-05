import streamlit as st
import torch
from torchvision import transforms
from PIL import Image



def main():
    st.title('Detect brain tumors')
    model = torch.hub.load(
        'ultralytics/yolov5',  # пути будем указывать гдето в локальном пространстве
        'custom',  # непредобученная
        path='best.pt',  # путь к нашим весам
    )
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    model.eval()
    model.conf = 0.88
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        results = model(image)
        st.image(results.render()[0], caption='Detection Result', use_column_width=True)


if __name__ == "__main__":
    main()
