import streamlit as st
from PIL import Image
from img_classification import *

st.sidebar.markdown("Welcome to Picture-lytics.")
st.sidebar.selectbox("Link to the relevant datasets.", ["https://www.kaggle.com/vipoooool/new-plant-diseases-dataset",
                                                        "https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection"])# kaggle links to dataset
page = st.sidebar.selectbox("Choose task", ["Plant Disease Classification", "Brain Tumor MRI Classification"])# pages

if page == "Plant Disease Classification":

    st.title("Image Classification with Google's Teachable Machine")
    st.header("Plant Leaf Disease Classification Example")
    st.write("Upload plant leaf images for quick analysis")
    # file upload and handling logic
    uploaded_file = st.file_uploader("Choose a maize(corn) leaf image ...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded corn leaf image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'model/corn_leaf_classification.h5')
        if label == 0:
            st.write("The image depicts healthy_corn")
        elif label == 1:
            st.write("The image depicts Common_rust")
        elif label == 2:
            st.write("The image depicts Cercospora_leaf_spot Gray_leaf_spot")
        elif label == 3:
            st.write("The image depicts Nothern_leaf_blight")
        else:
            st.write("Error")


elif page == "Brain Tumor MRI Classification":

    st.title("Image Classification with Google's Teachable Machine")
    st.header("Brain Tumor MRI Classification Example")
    st.text("Upload a brain MRI Image for image classification as tumor or no-tumor")
    # file upload and handling logic
    uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded MRI.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'model/brain_tumor_classification.h5')
        if label == 0:
            st.write("The MRI scan has a brain tumor")
        else:
            st.write("The MRI scan is healthy")