import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Aadhaar Verifier AI")
st.title("Document Verifier AI")
st.write("AIML Project - Blurry & Fake Detector")

uploaded = st.file_uploader("Aadhaar photo upload kar", type=['jpg','png','jpeg'])

def check_blur(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    score = cv2.Laplacian(gray, cv2.CV_64F).var()
    return score

if uploaded:
    img = Image.open(uploaded)
    st.image(img, width=300)
    score = check_blur(img)
    st.write(f"Blur Score: {score:.2f}")
    if score < 60:
        st.error("BLURRY AAHE - Photo parat kadha")
    else:
        st.success("CLEAR AAHE")