import io
import asyncio
from PIL import Image
import streamlit as st
from openai import OpenAI
from streamlit.runtime.scriptrunner import RerunException

# Initialize API key
if "API_KEY" not in st.session_state:
    st.session_state.API_KEY = None

# Sidebar for Configuration
with st.sidebar:
    st.title("🔧 Configuration")
    if not st.session_state.API_KEY:
        api_key = st.text_input("Enter API Key:", type="password")
        if st.button("Save Key"):
            st.session_state.API_KEY = api_key
            st.success("API Key saved!")
            st.experimental_rerun()
    else:
        st.success("API Key configured!")
        if st.button("Reset Key"):
            st.session_state.API_KEY = None
            st.experimental_rerun()

# Image Upload Section
st.title("🏥 Medical Imaging Diagnosis")
st.write("Upload a medical image to receive AI-powered diagnostic insights.")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "dicom"])

# Process and Analyze Image
if uploaded_file:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Open and display image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                try:
                    # Convert image to bytes
                    image_bytes = io.BytesIO()
                    image.save(image_bytes, format="PNG")
                    image_bytes.seek(0)

                    # Generate analysis
                    query = "Analyze this medical image and provide diagnostic insights."
                    response = OpenAI.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "system", "content": query}],
                    )
                    st.markdown("### 📋 Results")
                    st.write(response["choices"][0]["message"]["content"])
                except Exception as e:
                    st.error(f"Error during analysis: {e}")
else:
    st.info("Please upload an image to get started.")
