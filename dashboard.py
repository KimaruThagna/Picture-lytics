import streamlit as st

page = st.sidebar.selectbox("Choose task", ["Plant Disease Classification", "Brain Tumor MRI Classification"])

if page == "Plant Disease Classification":
    st.header("Plant Disease Classification")
    st.title("Plant Disease Classification")
    st.write("Upload plant images")

elif page == "Brain Tumor MRI Classification":
    st.title("Brain Tumor MRI Classification")
    st.text("Upload a brain MRI Image for image classification as tumor or no-tumor")