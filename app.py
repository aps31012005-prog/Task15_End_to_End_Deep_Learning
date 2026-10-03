
import os
import streamlit as st
import requests
from PIL import Image

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="CIFAR-10 Deep Learning App",
    page_icon="🧠",
    layout="wide"
)

# ==========================================
# Flask API Configuration
# ==========================================

FLASK_API_URL = os.getenv(
    "FLASK_API_URL",
    "http://flask-api:5000"
)

# ==========================================
# Application Title
# ==========================================

st.title("🧠 CIFAR-10 Deep Learning Image Classifier")
st.write(
    "Upload an image and the deep learning model will "
    "predict its CIFAR-10 class."
)

st.divider()

# ==========================================
# Image Upload
# ==========================================

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Prediction")

        if st.button("🔮 Predict Image"):

            try:
                files = {
                    "image": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }

                response = requests.post(
                    f"{FLASK_API_URL}/predict",
                    files=files,
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    predicted_class = result["predicted_class"]
                    confidence = result["confidence"]

                    st.success(
                        f"Predicted Class: {predicted_class}"
                    )

                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )

                else:

                    st.error(
                        f"API Error: {response.status_code}"
                    )

            except requests.exceptions.RequestException as e:

                st.error(
                    "Unable to connect to Flask API."
                )

                st.write(str(e))
