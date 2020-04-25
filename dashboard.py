import streamlit as st

st.sidebar.markdown("Welcome to Picture-lytics.")
st.sidebar.selectbox("Link to the relevant datasets.", ["link 1","link 2"])
page = st.sidebar.selectbox("Choose task", ["Plant Disease Classification", "Brain Tumor MRI Classification"])

if page == "Plant Disease Classification":
    st.header("Plant Disease Classification Example")
    st.title("Image Classification with Google's Teachable Machine")
    st.write("Upload plant images")

elif page == "Brain Tumor MRI Classification":
    st.title("Image Classification with Google's Teachable Machine")
    st.header("Brain Tumor MRI Classification Example")
    st.text("Upload a brain MRI Image for image classification as tumor or no-tumor")