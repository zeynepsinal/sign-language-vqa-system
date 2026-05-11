import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Sign Language VQA",
    page_icon="🤟",
    layout="centered"
)

CLASS_NAMES = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "del", "nothing", "space"
]

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("asl_alphabet_model_fast.keras")

model = load_model()

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((160, 160))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image, verbose=0)

    class_index = np.argmax(predictions)
    confidence = float(np.max(predictions))
    predicted_label = CLASS_NAMES[class_index]

    return predicted_label, confidence

def answer_question(question, label, confidence):
    question = question.lower()

    if "hangi harf" in question or "harf" in question or "what letter" in question:
        return f"Bu görselde modelin tahmin ettiği harf: {label}"

    elif "emin" in question or "güven" in question or "confidence" in question:
        return f"Model bu tahminden %{confidence * 100:.2f} oranında emin."

    else:
        return (
            "Bu sistem şu anda yalnızca işaret dili görselinden harf tahmini "
            "ve güven skoru verebilmektedir. Daha karmaşık soruları anlayamamaktadır."
        )
st.title("🤟 Sign Language VQA System")

st.write(
    "Bir işaret dili görseli yükleyin. Sistem görseldeki harfi tahmin eder "
    "ve sorduğunuz soruya göre cevap verir."
)

uploaded_file = st.file_uploader(
    "Görsel yükle",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Yüklenen Görsel", use_container_width=True)

    label, confidence = predict(image)

    st.subheader("❓ Soru Sor")
    question = st.text_input(
        "Örnek: Bu görselde hangi harf var?"
    )

    if question:
        response = answer_question(question, label, confidence)

        st.subheader("💬 Sistem Cevabı")
        st.write(response)