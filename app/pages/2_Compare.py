import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image
import cv2

st.set_page_config(
    page_title="🔍 Compare Breeds",
    page_icon="🔍",
    layout="wide"
)

# ── Load Model ───────────────────────────────────────
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model/best_model.h5")
    with open("model/class_names.json", "r") as f:
        class_names = json.load(f)
    return model, class_names

model, class_names = load_model()

breed_info = {
    "Gir_cow_India":             "🐄 Gir — High milk yield, from Gujarat",
    "Sahiwal_cow_India":         "🐄 Sahiwal — Best dairy breed, from Punjab",
    "Ongole_cow_India":          "🐄 Ongole — Strong draught breed, from Andhra Pradesh",
    "Kankrej_cow_India":         "🐄 Kankrej — Dual purpose, from Gujarat/Rajasthan",
    "Tharparkar_cow_India":      "🐄 Tharparkar — Desert hardy breed, from Rajasthan",
    "Murrah_buffalo_India":      "🐃 Murrah — World's best milk buffalo, from Haryana",
    "Nili_Ravi_buffalo_India":   "🐃 Nili-Ravi — High fat milk, from Punjab",
    "Surti_buffalo_India":       "🐃 Surti — Good milk quality, from Gujarat",
    "Jaffarabadi_buffalo_India": "🐃 Jaffarabadi — Heaviest buffalo, from Gujarat"
}

# ── Predict Function ─────────────────────────────────
def predict_breed(img):
    img_resized = img.resize((224, 224))
    img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)
    predictions = model.predict(img_array)[0]
    return predictions

# ── Human Face Detection ─────────────────────────────
def has_human_face(pil_img):
    img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0

# ── UI ───────────────────────────────────────────────
st.title("🔍 Compare Two Cattle/Buffalo Images")
st.markdown("Upload **two images** to compare their breed predictions side by side!")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🖼️ Image 1")
    upload1 = st.file_uploader(
        "Upload first image",
        type=["jpg", "jpeg", "png"],
        key="img1"
    )

with col2:
    st.subheader("🖼️ Image 2")
    upload2 = st.file_uploader(
        "Upload second image",
        type=["jpg", "jpeg", "png"],
        key="img2"
    )

# ── Process Both Images ──────────────────────────────
if upload1 and upload2:
    img1 = Image.open(upload1).convert("RGB")
    img2 = Image.open(upload2).convert("RGB")

    col1, col2 = st.columns(2)
    with col1:
        st.image(img1, use_container_width=True, caption="Image 1")
    with col2:
        st.image(img2, use_container_width=True, caption="Image 2")

    st.markdown("---")

    # ── Human Face Check ─────────────────────────────
    if has_human_face(img1):
        st.error("⚠️ Image 1 contains a human face! Please upload cattle or buffalo only.")
        st.stop()
    if has_human_face(img2):
        st.error("⚠️ Image 2 contains a human face! Please upload cattle or buffalo only.")
        st.stop()

    # ── Predict Both ──────────────────────────────────
    with st.spinner("🔍 Analyzing both images..."):
        pred1 = predict_breed(img1)
        pred2 = predict_breed(img2)

    top1_idx = np.argmax(pred1)
    top2_idx = np.argmax(pred2)

    breed1_key = class_names[str(top1_idx)]
    breed2_key = class_names[str(top2_idx)]

    top1_conf = pred1[top1_idx] * 100
    top2_conf = pred2[top2_idx] * 100

    # ── Block Other/Unknown ───────────────────────────
    if "Other" in breed1_key or top1_conf < 30:
        st.error("⚠️ Image 1 does not appear to be a cattle or buffalo!")
        st.stop()
    if "Other" in breed2_key or top2_conf < 30:
        st.error("⚠️ Image 2 does not appear to be a cattle or buffalo!")
        st.stop()

    breed1_name = breed1_key.replace("_India", "").replace("_", " ").title()
    breed2_name = breed2_key.replace("_India", "").replace("_", " ").title()

    conf1 = pred1[top1_idx] * 100
    conf2 = pred2[top2_idx] * 100

    # ── Results ──────────────────────────────────────
    st.subheader("📊 Comparison Results")
    col1, col2 = st.columns(2)

    with col1:
        st.success(f"✅ **{breed1_name}**")
        st.metric("Confidence", f"{conf1:.1f}%")
        if conf1 < 40:
            st.warning("⚠️ Low confidence!")
        st.info(breed_info.get(breed1_key, "Indian breed"))
        st.markdown("**Top 3 Predictions:**")
        for idx in np.argsort(pred1)[::-1][:3]:
            bname = class_names[str(idx)].replace("_India","").replace("_"," ").title()
            st.write(f"• {bname}: {pred1[idx]*100:.1f}%")

    with col2:
        st.success(f"✅ **{breed2_name}**")
        st.metric("Confidence", f"{conf2:.1f}%")
        if conf2 < 40:
            st.warning("⚠️ Low confidence!")
        st.info(breed_info.get(breed2_key, "Indian breed"))
        st.markdown("**Top 3 Predictions:**")
        for idx in np.argsort(pred2)[::-1][:3]:
            bname = class_names[str(idx)].replace("_India","").replace("_"," ").title()
            st.write(f"• {bname}: {pred2[idx]*100:.1f}%")

    # ── Verdict ──────────────────────────────────────
    st.markdown("---")
    st.subheader("🏆 Verdict")
    if breed1_key == breed2_key:
        st.success(f"✅ Both images are predicted as the **same breed — {breed1_name}!**")
    else:
        st.info(f"🔄 Image 1 is **{breed1_name}** and Image 2 is **{breed2_name}** — different breeds!")

    if conf1 > conf2:
        st.info(f"📈 Image 1 has higher confidence ({conf1:.1f}% vs {conf2:.1f}%)")
    elif conf2 > conf1:
        st.info(f"📈 Image 2 has higher confidence ({conf2:.1f}% vs {conf1:.1f}%)")
    else:
        st.info("📈 Both images have equal confidence!")

else:
    st.info("👆 Please upload both images to start comparison!")