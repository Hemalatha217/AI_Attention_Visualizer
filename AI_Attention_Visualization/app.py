import streamlit as st
import numpy as np
from PIL import Image

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention

st.set_page_config(
    page_title="Smart OCR Attention System",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Smart OCR Attention System")
st.write("Upload an image to extract text and analyze word attention.")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    text = extract_text(image)

    st.subheader("📝 Extracted Text")

    if not text.strip():
        st.error("No text found in the image.")
        st.stop()

    st.write(text)

    words = text.split()

    words = [
        word.strip(".,!?;:()[]{}\"'")
        for word in words
    ]

    words = [
        word
        for word in words
        if len(word) > 2
    ]

    words = words[:20]

    embeddings = create_embeddings(words)

    attention_scores = calculate_attention(embeddings)

    normalized_scores = (
        attention_scores / attention_scores.max()
    )

    st.subheader("🧠 Attention Scores")

    for word, score in zip(words, normalized_scores):
        st.write(f"**{word}** : {score:.2f}")
        st.progress(float(score))

    top_index = np.argmax(attention_scores)

    st.success(
        f"🏆 Most Important Word: {words[top_index]}"
    )

    st.subheader("📋 Score Summary")

    for word, score in zip(words, normalized_scores):
        st.text(f"{word:<20} {score:.2f}")

