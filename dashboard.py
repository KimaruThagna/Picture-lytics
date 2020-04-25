import streamlit as st
from PIL import Image


st.sidebar.markdown("Welcome to Picture-lytics.")
st.sidebar.selectbox("Link to the relevant datasets.", ["link 1","link 2"])# kaggle links to dataset
page = st.sidebar.selectbox("Choose task", ["Plant Disease Classification", "Brain Tumor MRI Classification"])# pages

if page == "Plant Disease Classification":

    st.title("Image Classification with Google's Teachable Machine")
    st.header("Plant Leaf Disease Classification Example")
    st.write("Upload plant leaf images for quick analysis")
    # file upload and handling logic
    uploaded_file = st.file_uploader("Choose a maize(corn) leaf image ...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded MRI.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = predict(uploaded_file)
        st.write("")

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
        label = predict(uploaded_file)
        st.write("")