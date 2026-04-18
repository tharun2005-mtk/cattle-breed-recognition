# # # # Streamlit app
# # # # ── Add this import at the top ───────────────────────
# # # import cv2
# # # import numpy as np
# # # import streamlit as st
# # # import tensorflow as tf
# # # import numpy as np
# # # from PIL import Image
# # # import json
# # # import os

# # # os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # # # ── Page Config ──────────────────────────────────────
# # # st.set_page_config(
# # #     page_title="🐄 Cattle Breed Recognizer",
# # #     page_icon="🐄",
# # #     layout="centered"
# # # )

# # # # ── Load Model & Class Names ─────────────────────────
# # # @st.cache_resource
# # # def load_model():
# # #     model = tf.keras.models.load_model("model/best_model.h5")
# # #     with open("model/class_names.json", "r") as f:
# # #         class_names = json.load(f)
# # #     return model, class_names

# # # model, class_names = load_model()

# # # # ── Breed Info Dictionary ────────────────────────────
# # # breed_info = {
# # #     "Gir_cow_India":             "🐄 Gir is one of the principal Zebu breeds originating from Gujarat, India. Known for high milk yield.",
# # #     "Sahiwal_cow_India":         "🐄 Sahiwal is a high milk-producing breed from Punjab. One of the best dairy breeds in India.",
# # #     "Ongole_cow_India":          "🐄 Ongole is a large draught breed from Andhra Pradesh, known for strength and heat tolerance.",
# # #     "Kankrej_cow_India":         "🐄 Kankrej is a dual-purpose breed from Gujarat/Rajasthan, used for both milk and draught work.",
# # #     "Tharparkar_cow_India":      "🐄 Tharparkar is a hardy breed from Rajasthan desert, known for surviving in dry conditions.",
# # #     "Murrah_buffalo_India":      "🐃 Murrah is the world's highest milk-producing buffalo breed, originating from Haryana.",
# # #     "Nili_Ravi_buffalo_India":   "🐃 Nili-Ravi is a high-yielding buffalo breed from Punjab, known for rich fat content in milk.",
# # #     "Surti_buffalo_India":       "🐃 Surti is a medium-sized buffalo from Gujarat, known for good milk quality.",
# # #     "Jaffarabadi_buffalo_India": "🐃 Jaffarabadi is the heaviest buffalo breed from Gujarat, known for high milk fat."
# # # }

# # # # ── UI Header ────────────────────────────────────────
# # # st.title("🐄 Indian Cattle & Buffalo Breed Recognizer")
# # # st.markdown("Upload an image of a **cow or buffalo** to identify its breed using AI!")
# # # st.markdown("---")

# # # # ── File Uploader ────────────────────────────────────
# # # uploaded = st.file_uploader(
# # #     "📁 Upload an image (JPG, JPEG, PNG)",
# # #     type=["jpg", "jpeg", "png"]
# # # )

# # # if uploaded is not None:
# # #     col1, col2 = st.columns(2)

# # #     with col1:
# # #         st.subheader("📸 Uploaded Image")
# # #         img = Image.open(uploaded).convert("RGB")
# # #         st.image(img, use_container_width=True)

# # #     # ── Preprocess & Predict ─────────────────────────
# # #     img_resized = img.resize((224, 224))
# # #     img_array = np.array(img_resized) / 255.0
# # #     img_array = np.expand_dims(img_array, axis=0)

# # #     # with st.spinner("🔍 Analyzing breed..."):
# # #     #     predictions = model.predict(img_array)[0]

# # #     # ── Validate image before predicting ─────────────────
# # # def is_valid_animal_image(pil_img):
# # #     img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
# # #     # Check if human face exists
# # #     face_cascade = cv2.CascadeClassifier(
# # #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# # #     )
# # #     gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# # #     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# # #     if len(faces) > 0:
# # #         return False  # Human face detected
# # #     return True

# # # with st.spinner("🔍 Analyzing image..."):
# # #     if not is_valid_animal_image(img):
# # #         st.error("⚠️ No cattle or buffalo detected in this image. Please upload a valid cow or buffalo photo!")
# # #         st.stop()
# # #     predictions = model.predict(img_array)[0]

# # #     top3_indices = np.argsort(predictions)[::-1][:3]

# # #     with col2:
# # #         st.subheader("🔍 Prediction Results")
# # #         for i, idx in enumerate(top3_indices):
# # #             breed_key = class_names[str(idx)]
# # #             breed_display = breed_key.replace("_India", "").replace("_", " ").title()
# # #             confidence = predictions[idx] * 100

# # #             if i == 0:
# # #                 st.success(f"✅ **{breed_display}**")
# # #                 st.metric("Confidence", f"{confidence:.1f}%")
# # #             else:
# # #                 st.info(f"#{i+1} {breed_display} — {confidence:.1f}%")

# # #     # ── Breed Info ───────────────────────────────────
# # #     st.markdown("---")
# # #     top_breed_key = class_names[str(top3_indices[0])]
# # #     top_breed_display = top_breed_key.replace("_India", "").replace("_", " ").title()

# # #     st.subheader(f"📖 About {top_breed_display}")
# # #     info = breed_info.get(top_breed_key, "A native Indian cattle/buffalo breed.")
# # #     st.info(info)

# # #     # ── Confidence Bar Chart ─────────────────────────
# # #     st.markdown("---")
# # #     st.subheader("📊 Confidence Scores (Top 5)")
# # #     top5_indices = np.argsort(predictions)[::-1][:5]
# # #     for idx in top5_indices:
# # #         breed_key = class_names[str(idx)]
# # #         breed_display = breed_key.replace("_India", "").replace("_", " ").title()
# # #         conf = predictions[idx]
# # #         st.progress(float(conf), text=f"{breed_display}: {conf*100:.1f}%")

# # # else:
# # #     st.markdown("### 👆 Upload an image to get started!")
# # #     st.markdown("""
# # #     **Supported Breeds:**
# # #     | Cattle 🐄 | Buffalo 🐃 |
# # #     |---|---|
# # #     | Gir | Murrah |
# # #     | Sahiwal | Nili-Ravi |
# # #     | Ongole | Surti |
# # #     | Kankrej | Jaffarabadi |
# # #     | Tharparkar | |
# # #     """)


# # import os
# # os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # import streamlit as st
# # import tensorflow as tf
# # import numpy as np
# # import cv2
# # import json
# # from PIL import Image

# # # ── Page Config ──────────────────────────────────────
# # st.set_page_config(
# #     page_title="🐄 Cattle Breed Recognizer",
# #     page_icon="🐄",
# #     layout="centered"
# # )

# # # ── Load Model & Class Names ─────────────────────────
# # @st.cache_resource
# # def load_model():
# #     model = tf.keras.models.load_model("model/best_model.h5")
# #     with open("model/class_names.json", "r") as f:
# #         class_names = json.load(f)
# #     return model, class_names

# # model, class_names = load_model()

# # # ── Breed Info ───────────────────────────────────────
# # breed_info = {
# #     "Gir_cow_India":             "🐄 Gir is one of the principal Zebu breeds from Gujarat. Known for high milk yield.",
# #     "Sahiwal_cow_India":         "🐄 Sahiwal is a high milk-producing breed from Punjab. One of the best dairy breeds in India.",
# #     "Ongole_cow_India":          "🐄 Ongole is a large draught breed from Andhra Pradesh, known for strength and heat tolerance.",
# #     "Kankrej_cow_India":         "🐄 Kankrej is a dual-purpose breed from Gujarat/Rajasthan, used for milk and draught work.",
# #     "Tharparkar_cow_India":      "🐄 Tharparkar is a hardy breed from Rajasthan desert, known for surviving in dry conditions.",
# #     "Murrah_buffalo_India":      "🐃 Murrah is the world's highest milk-producing buffalo breed, originating from Haryana.",
# #     "Nili_Ravi_buffalo_India":   "🐃 Nili-Ravi is a high-yielding buffalo breed from Punjab, known for rich fat content in milk.",
# #     "Surti_buffalo_India":       "🐃 Surti is a medium-sized buffalo from Gujarat, known for good milk quality.",
# #     "Jaffarabadi_buffalo_India": "🐃 Jaffarabadi is the heaviest buffalo breed from Gujarat, known for high milk fat."
# # }

# # # ── Human Face Detection ─────────────────────────────
# # def has_human_face(pil_img):
# #     img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
# #     face_cascade = cv2.CascadeClassifier(
# #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# #     )
# #     gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# #     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# #     return len(faces) > 0

# # # ── UI Header ────────────────────────────────────────
# # st.title("🐄 Indian Cattle & Buffalo Breed Recognizer")
# # st.markdown("Upload an image of a **cow or buffalo** to identify its breed using AI!")
# # st.markdown("---")

# # # ── File Uploader ────────────────────────────────────
# # uploaded = st.file_uploader(
# #     "📁 Upload an image (JPG, JPEG, PNG)",
# #     type=["jpg", "jpeg", "png"]
# # )

# # if uploaded is not None:
# #     img = Image.open(uploaded).convert("RGB")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.subheader("📸 Uploaded Image")
# #         # st.image(img, use_container_width=True)
# #         st.image(img, width='stretch')

# #     # ── Human Face Check ─────────────────────────────
# #     if has_human_face(img):
# #         with col2:
# #             st.subheader("🔍 Prediction Results")
# #             st.error("⚠️ Human face detected! Please upload a cattle or buffalo image only.")
# #         st.stop()

# #     # ── Preprocess & Predict ─────────────────────────
# #     img_resized = img.resize((224, 224))
# #     img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)

# #     with st.spinner("🔍 Analyzing breed..."):
# #         predictions = model.predict(img_array)[0]

# #     top3_indices = np.argsort(predictions)[::-1][:3]

# #     with col2:
# #         st.subheader("🔍 Prediction Results")
# #         for i, idx in enumerate(top3_indices):
# #             breed_key = class_names[str(idx)]
# #             breed_display = breed_key.replace("_India", "").replace("_", " ").title()
# #             confidence = predictions[idx] * 100
# #             if i == 0:
# #                 st.success(f"✅ **{breed_display}**")
# #                 st.metric("Confidence", f"{confidence:.1f}%")
# #             else:
# #                 st.info(f"#{i+1} {breed_display} — {confidence:.1f}%")

# #     # ── Breed Info ───────────────────────────────────
# #     st.markdown("---")
# #     top_breed_key = class_names[str(top3_indices[0])]
# #     top_breed_display = top_breed_key.replace("_India", "").replace("_", " ").title()
# #     st.subheader(f"📖 About {top_breed_display}")
# #     st.info(breed_info.get(top_breed_key, "A native Indian cattle/buffalo breed."))

# #     # ── Confidence Bar Chart ─────────────────────────
# #     st.markdown("---")
# #     st.subheader("📊 Confidence Scores (Top 5)")
# #     top5_indices = np.argsort(predictions)[::-1][:5]
# #     for idx in top5_indices:
# #         breed_key = class_names[str(idx)]
# #         breed_display = breed_key.replace("_India", "").replace("_", " ").title()
# #         conf = float(predictions[idx])
# #         st.progress(conf, text=f"{breed_display}: {conf*100:.1f}%")

# # else:
# #     st.markdown("### 👆 Upload an image to get started!")
# #     st.markdown("""
# #     **Supported Breeds:**
# #     | Cattle 🐄 | Buffalo 🐃 |
# #     |---|---|
# #     | Gir | Murrah |
# #     | Sahiwal | Nili-Ravi |
# #     | Ongole | Surti |
# #     | Kankrej | Jaffarabadi |
# #     | Tharparkar | |
# #     """)


# import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# import streamlit as st
# import tensorflow as tf
# import numpy as np
# import cv2
# import json
# from PIL import Image
# import datetime

# # ── Page Config ──────────────────────────────────────
# st.set_page_config(
#     page_title="🐄 Cattle Breed Recognizer",
#     page_icon="🐄",
#     layout="centered"
# )

# # ── Load Model & Class Names ─────────────────────────
# @st.cache_resource
# def load_model():
#     model = tf.keras.models.load_model("model/best_model.h5")
#     with open("model/class_names.json", "r") as f:
#         class_names = json.load(f)
#     return model, class_names

# model, class_names = load_model()

# # ── Breed Info ───────────────────────────────────────
# breed_info = {
#     "Gir_cow_India":             "🐄 Gir is one of the principal Zebu breeds from Gujarat. Known for high milk yield.",
#     "Sahiwal_cow_India":         "🐄 Sahiwal is a high milk-producing breed from Punjab. One of the best dairy breeds in India.",
#     "Ongole_cow_India":          "🐄 Ongole is a large draught breed from Andhra Pradesh, known for strength and heat tolerance.",
#     "Kankrej_cow_India":         "🐄 Kankrej is a dual-purpose breed from Gujarat/Rajasthan, used for milk and draught work.",
#     "Tharparkar_cow_India":      "🐄 Tharparkar is a hardy breed from Rajasthan desert, known for surviving in dry conditions.",
#     "Murrah_buffalo_India":      "🐃 Murrah is the world's highest milk-producing buffalo breed, originating from Haryana.",
#     "Nili_Ravi_buffalo_India":   "🐃 Nili-Ravi is a high-yielding buffalo breed from Punjab, known for rich fat content in milk.",
#     "Surti_buffalo_India":       "🐃 Surti is a medium-sized buffalo from Gujarat, known for good milk quality.",
#     "Jaffarabadi_buffalo_India": "🐃 Jaffarabadi is the heaviest buffalo breed from Gujarat, known for high milk fat."
# }

# # ── Breed Image URLs ─────────────────────────────────
# breed_images = {
#     "Gir_cow_India":             "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Gyr_Bull.jpg/320px-Gyr_Bull.jpg",
#     "Sahiwal_cow_India":         "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Sahiwal_Bull.jpg/320px-Sahiwal_Bull.jpg",
#     "Ongole_cow_India":          "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Ongole_Bull.jpg/320px-Ongole_Bull.jpg",
#     "Kankrej_cow_India":         "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Kankrej_bull.jpg/320px-Kankrej_bull.jpg",
#     "Tharparkar_cow_India":      "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tharparkar_cow.jpg/320px-Tharparkar_cow.jpg",
#     "Murrah_buffalo_India":      "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Murrah_Buffalo.jpg/320px-Murrah_Buffalo.jpg",
#     "Nili_Ravi_buffalo_India":   "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Nili_Ravi_Buffalo.jpg/320px-Nili_Ravi_Buffalo.jpg",
#     "Surti_buffalo_India":       "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Surti_buffalo.jpg/320px-Surti_buffalo.jpg",
#     "Jaffarabadi_buffalo_India": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jaffarabadi_buffalo.jpg/320px-Jaffarabadi_buffalo.jpg"
# }

# # ── Human Face Detection ─────────────────────────────
# # def has_human_face(pil_img):
# #     img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
# #     face_cascade = cv2.CascadeClassifier(
# #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# #     )
# #     gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# #     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# #     return len(faces) > 0

# # def is_invalid_image(pil_img):
#     # img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
#     # # Check 1: Human face detection
#     # face_cascade = cv2.CascadeClassifier(
#     #     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
#     # )
#     # gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
#     # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     # if len(faces) > 0:
#     #     return True, "Human face detected!"

#     # # Check 2: Image must have natural colors (not screenshots/diagrams)
#     # hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
#     # saturation = hsv[:, :, 1].mean()
#     # if saturation < 30:
#     #     return True, "Image appears to be a screenshot or diagram!"

#     # # Check 3: Image must have enough color variation (natural photo)
#     # std_dev = img_cv.std()
#     # if std_dev < 20:
#     #     return True, "Image is too uniform — please upload a real photo!"

#     # return False, ""

# # def is_invalid_image(pil_img):
# #     img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
# #     face_cascade = cv2.CascadeClassifier(
# #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# #     )
# #     gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# #     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# #     if len(faces) > 0:
# #         return True, "Human face detected!"
# #     edges = cv2.Canny(gray, 50, 150)
# #     lines = cv2.HoughLinesP(edges, 1, np.pi/180,
# #                             threshold=100,
# #                             minLineLength=100,
# #                             maxLineGap=10)
# #     if lines is not None and len(lines) > 20:
# #         return True, "Image appears to be a diagram or screenshot!"
# #     hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
# #     white_mask = cv2.inRange(hsv, (0, 0, 200), (180, 30, 255))
# #     white_ratio = np.sum(white_mask > 0) / (img_cv.shape[0] * img_cv.shape[1])
# #     if white_ratio > 0.4:
# #         return True, "Image appears to be a document or screenshot!"
# #     saturation = hsv[:, :, 1].mean()
# #     if saturation < 25:
# #         return True, "Image does not appear to be a natural photo!"
# #     return False, ""

# # def is_invalid_image(pil_img):
# #     img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
# #     face_cascade = cv2.CascadeClassifier(
# #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# #     )
# #     gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# #     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# #     if len(faces) > 0:
# #         return True, "Human face detected!"
# #     edges = cv2.Canny(gray, 50, 150)
# #     lines = cv2.HoughLinesP(edges, 1, np.pi/180,
# #                             threshold=100,
# #                             minLineLength=100,
# #                             maxLineGap=10)
# #     if lines is not None and len(lines) > 20:
# #         return True, "Image appears to be a diagram or screenshot!"
# #     hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
# #     white_mask = cv2.inRange(hsv, (0, 0, 200), (180, 30, 255))
# #     white_ratio = np.sum(white_mask > 0) / (img_cv.shape[0] * img_cv.shape[1])
# #     if white_ratio > 0.4:
# #         return True, "Image appears to be a document or screenshot!"
# #     saturation = hsv[:, :, 1].mean()
# #     if saturation < 25:
# #         return True, "Image does not appear to be a natural photo!"
# #     return False, ""

# # ── Predict Function ─────────────────────────────────
# def predict_breed(img):
#     img_resized = img.resize((224, 224))
#     img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)
#     predictions = model.predict(img_array)[0]
#     return predictions

# # ── Initialize History ───────────────────────────────
# if "history" not in st.session_state:
#     st.session_state.history = []

# # ── UI Header ────────────────────────────────────────
# st.title("🐄 Indian Cattle & Buffalo Breed Recognizer")
# st.markdown("Upload an image of a **cow or buffalo** to identify its breed using AI!")
# st.markdown("---")

# # ── File Uploader ────────────────────────────────────
# uploaded = st.file_uploader(
#     "📁 Upload an image (JPG, JPEG, PNG)",
#     type=["jpg", "jpeg", "png"]
# )

# if uploaded is not None:
#     img = Image.open(uploaded).convert("RGB")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("📸 Uploaded Image")
#         st.image(img, width='stretch')

#     # ── Human Face Check ─────────────────────────────
#     # if has_human_face(img):
#     #     with col2:
#     #         st.subheader("🔍 Prediction Results")
#     #         st.error("⚠️ Human face detected! Please upload a cattle or buffalo image only.")
#     #     st.stop()

#     # invalid, reason = is_invalid_image(img)
#     # if invalid:
#     #     with col2:
#     #         st.subheader("🔍 Prediction Results")
#     #         st.error(f"⚠️ {reason} Please upload a real cattle or buffalo photo only.")
#     #     st.stop()

#     if has_human_face(img):
#         with col2:
#             st.subheader("🔍 Prediction Results")
#             st.error("⚠️ Human face detected! Please upload a cattle or buffalo image only.")
#         st.stop()

#     # ── Predict ──────────────────────────────────────
#     with st.spinner("🔍 Analyzing breed..."):
#         predictions = predict_breed(img)

#     top3_indices = np.argsort(predictions)[::-1][:3]
#     top_breed_key = class_names[str(top3_indices[0])]
#     top_confidence = predictions[top3_indices[0]] * 100
#     # ── Block "Other" class predictions ──────────────────
#     # if "Other" in top_breed_key:
#     #     with col2:
#     #         st.subheader("🔍 Prediction Results")
#     #         st.error("⚠️ This does not appear to be a cattle or buffalo image!")
#     #         st.warning("Please upload a valid Indian cattle or buffalo photo.")
#     #     st.stop()

#     if "Other" in top_breed_key or top_confidence < 45:
#         with col2:
#             st.subheader("🔍 Prediction Results")
#             st.error("⚠️ This does not appear to be a cattle or buffalo image!")
#             st.warning("Please upload a valid Indian cattle or buffalo photo.")
#         st.stop()

#     with col2:
#         st.subheader("🔍 Prediction Results")

#         # ── Confidence Threshold Warning ─────────────
#         # if top_confidence < 40:
#         #     st.warning(f"⚠️ Low confidence ({top_confidence:.1f}%)! The image may not be clear or the breed may not be in our dataset.")
#         # ── Confidence Threshold Block ────────────────────
#         if top_confidence < 25:
#             st.error(f"⚠️ Could not confidently identify a cattle/buffalo breed! (Confidence: {top_confidence:.1f}%)")
#             st.warning("Please upload a **clear image** of an Indian cattle or buffalo breed.")
#             st.stop()

#         for i, idx in enumerate(top3_indices):
#             breed_key = class_names[str(idx)]
#             breed_display = breed_key.replace("_India", "").replace("_", " ").title()
#             confidence = predictions[idx] * 100
#             if i == 0:
#                 st.success(f"✅ **{breed_display}**")
#                 st.metric("Confidence", f"{confidence:.1f}%")
#             else:
#                 st.info(f"#{i+1} {breed_display} — {confidence:.1f}%")

#     # ── Breed Info & Image ───────────────────────────
#     st.markdown("---")
#     top_breed_display = top_breed_key.replace("_India", "").replace("_", " ").title()
#     st.subheader(f"📖 About {top_breed_display}")

#     info_col, img_col = st.columns(2)
#     with info_col:
#         st.info(breed_info.get(top_breed_key, "A native Indian cattle/buffalo breed."))
#     with img_col:
#         img_url = breed_images.get(top_breed_key)
#         # if img_url:
#         #     st.image(img_url, caption=f"Reference: {top_breed_display}", width='stretch')
#         if img_url:
#             try:
#                 import requests
#                 from io import BytesIO
#                 response = requests.get(img_url, timeout=5)
#                 if response.status_code == 200:
#                     ref_img = Image.open(BytesIO(response.content))
#                     st.image(ref_img, caption=f"Reference: {top_breed_display}", width='stretch')
#                 else:
#                     st.caption(f"📖 Reference image unavailable")
#             except:
#                 st.caption(f"📖 Reference image unavailable")

#     # ── Confidence Bar Chart ─────────────────────────
#     st.markdown("---")
#     st.subheader("📊 Confidence Scores (Top 5)")
#     top5_indices = np.argsort(predictions)[::-1][:5]
#     for idx in top5_indices:
#         breed_key = class_names[str(idx)]
#         breed_display = breed_key.replace("_India", "").replace("_", " ").title()
#         conf = float(predictions[idx])
#         st.progress(conf, text=f"{breed_display}: {conf*100:.1f}%")

#     # ── Save to History ──────────────────────────────
#     st.session_state.history.append({
#         "time": datetime.datetime.now().strftime("%H:%M:%S"),
#         "breed": top_breed_display,
#         "confidence": f"{top_confidence:.1f}%",
#         "image": img
#     })
#     if len(st.session_state.history) > 5:
#         st.session_state.history.pop(0)

#     # ── Export PDF Button ────────────────────────────
#     st.markdown("---")
#     st.subheader("📄 Export Result")
#     if st.button("📥 Download Result as PDF"):
#         from fpdf import FPDF
#         import tempfile

#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", "B", 16)
#         pdf.cell(200, 10, "Cattle Breed Recognition Report", ln=True, align="C")
#         pdf.set_font("Arial", "", 12)
#         pdf.cell(200, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
#         pdf.cell(200, 10, f"Predicted Breed: {top_breed_display}", ln=True)
#         pdf.cell(200, 10, f"Confidence: {top_confidence:.1f}%", ln=True)
#         pdf.cell(200, 10, f"Info: {breed_info.get(top_breed_key, '')}", ln=True)

#         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
#             pdf.output(f.name)
#             with open(f.name, "rb") as pdf_file:
#                 st.download_button(
#                     label="📄 Click here to Download PDF",
#                     data=pdf_file.read(),
#                     file_name="breed_result.pdf",
#                     mime="application/pdf"
#                 )

# else:
#     st.markdown("### 👆 Upload an image to get started!")
#     st.markdown("""
#     **Supported Breeds:**
#     | Cattle 🐄 | Buffalo 🐃 |
#     |---|---|
#     | Gir | Murrah |
#     | Sahiwal | Nili-Ravi |
#     | Ongole | Surti |
#     | Kankrej | Jaffarabadi |
#     | Tharparkar | |
#     """)
#     st.markdown("---")
#     st.info("👈 Use the **sidebar** to navigate to Breed Info, Compare Images, and History pages!")

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import json
from PIL import Image
import datetime
import requests
from io import BytesIO

# ── Page Config ──────────────────────────────────────
st.set_page_config(
    page_title="🐄 Cattle Breed Recognizer",
    page_icon="🐄",
    layout="centered"
)

# ── Load Model & Class Names ─────────────────────────
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model/best_model.h5")
    with open("model/class_names.json", "r") as f:
        class_names = json.load(f)
    return model, class_names

model, class_names = load_model()

# ── Breed Info ───────────────────────────────────────
breed_info = {
    "Gir_cow_India":             "🐄 Gir is one of the principal Zebu breeds from Gujarat. Known for high milk yield.",
    "Sahiwal_cow_India":         "🐄 Sahiwal is a high milk-producing breed from Punjab. One of the best dairy breeds in India.",
    "Ongole_cow_India":          "🐄 Ongole is a large draught breed from Andhra Pradesh, known for strength and heat tolerance.",
    "Kankrej_cow_India":         "🐄 Kankrej is a dual-purpose breed from Gujarat/Rajasthan, used for milk and draught work.",
    "Tharparkar_cow_India":      "🐄 Tharparkar is a hardy breed from Rajasthan desert, known for surviving in dry conditions.",
    "Murrah_buffalo_India":      "🐃 Murrah is the world's highest milk-producing buffalo breed, originating from Haryana.",
    "Nili_Ravi_buffalo_India":   "🐃 Nili-Ravi is a high-yielding buffalo breed from Punjab, known for rich fat content in milk.",
    "Surti_buffalo_India":       "🐃 Surti is a medium-sized buffalo from Gujarat, known for good milk quality.",
    "Jaffarabadi_buffalo_India": "🐃 Jaffarabadi is the heaviest buffalo breed from Gujarat, known for high milk fat."
}

# ── Breed Image URLs ─────────────────────────────────
breed_images = {
    "Gir_cow_India":             "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Gyr_Bull.jpg/320px-Gyr_Bull.jpg",
    "Sahiwal_cow_India":         "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Sahiwal_Bull.jpg/320px-Sahiwal_Bull.jpg",
    "Ongole_cow_India":          "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Ongole_Bull.jpg/320px-Ongole_Bull.jpg",
    "Kankrej_cow_India":         "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Kankrej_bull.jpg/320px-Kankrej_bull.jpg",
    "Tharparkar_cow_India":      "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tharparkar_cow.jpg/320px-Tharparkar_cow.jpg",
    "Murrah_buffalo_India":      "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Murrah_Buffalo.jpg/320px-Murrah_Buffalo.jpg",
    "Nili_Ravi_buffalo_India":   "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Nili_Ravi_Buffalo.jpg/320px-Nili_Ravi_Buffalo.jpg",
    "Surti_buffalo_India":       "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Surti_buffalo.jpg/320px-Surti_buffalo.jpg",
    "Jaffarabadi_buffalo_India": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jaffarabadi_buffalo.jpg/320px-Jaffarabadi_buffalo.jpg"
}

# ── Human Face Detection ─────────────────────────────
def has_human_face(pil_img):
    img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0

# ── Predict Function ─────────────────────────────────
def predict_breed(img):
    img_resized = img.resize((224, 224))
    img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)
    predictions = model.predict(img_array)[0]
    return predictions

# ── Initialize History ───────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []

# ── UI Header ────────────────────────────────────────
st.title("🐄 Indian Cattle & Buffalo Breed Recognizer")
st.markdown("Upload an image of a **cow or buffalo** to identify its breed using AI!")
st.markdown("---")

# ── File Uploader ────────────────────────────────────
uploaded = st.file_uploader(
    "📁 Upload an image (JPG, JPEG, PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded is not None:
    img = Image.open(uploaded).convert("RGB")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📸 Uploaded Image")
        st.image(img, width='stretch')

    # ── Human Face Check ─────────────────────────────
    if has_human_face(img):
        with col2:
            st.subheader("🔍 Prediction Results")
            st.error("⚠️ Human face detected! Please upload a cattle or buffalo image only.")
        st.stop()

    # ── Predict ──────────────────────────────────────
    with st.spinner("🔍 Analyzing breed..."):
        predictions = predict_breed(img)

    top3_indices = np.argsort(predictions)[::-1][:3]
    top_breed_key = class_names[str(top3_indices[0])]
    top_confidence = predictions[top3_indices[0]] * 100

    # ── Block Other/Unknown images ────────────────────
    # if "Other" in top_breed_key or top_confidence < 45:
    if "Other" in top_breed_key or top_confidence < 30:
        with col2:
            st.subheader("🔍 Prediction Results")
            st.error("⚠️ This does not appear to be a cattle or buffalo image!")
            st.warning("Please upload a valid Indian cattle or buffalo photo.")
        st.stop()

    with col2:
        st.subheader("🔍 Prediction Results")
        for i, idx in enumerate(top3_indices):
            breed_key = class_names[str(idx)]
            breed_display = breed_key.replace("_India", "").replace("_", " ").title()
            confidence = predictions[idx] * 100
            if i == 0:
                st.success(f"✅ **{breed_display}**")
                st.metric("Confidence", f"{confidence:.1f}%")
            else:
                st.info(f"#{i+1} {breed_display} — {confidence:.1f}%")

    # ── Breed Info & Image ───────────────────────────
    st.markdown("---")
    top_breed_display = top_breed_key.replace("_India", "").replace("_", " ").title()
    st.subheader(f"📖 About {top_breed_display}")

    info_col, img_col = st.columns(2)
    with info_col:
        st.info(breed_info.get(top_breed_key, "A native Indian cattle/buffalo breed."))
    with img_col:
        img_url = breed_images.get(top_breed_key)
        if img_url:
            try:
                response = requests.get(img_url, timeout=5)
                if response.status_code == 200:
                    ref_img = Image.open(BytesIO(response.content))
                    st.image(ref_img, caption=f"Reference: {top_breed_display}", width='stretch')
                else:
                    st.caption("📖 Reference image unavailable")
            except:
                st.caption("📖 Reference image unavailable")

    # ── Confidence Bar Chart ─────────────────────────
    st.markdown("---")
    st.subheader("📊 Confidence Scores (Top 5)")
    top5_indices = np.argsort(predictions)[::-1][:5]
    for idx in top5_indices:
        breed_key = class_names[str(idx)]
        breed_display = breed_key.replace("_India", "").replace("_", " ").title()
        conf = float(predictions[idx])
        st.progress(conf, text=f"{breed_display}: {conf*100:.1f}%")

    # ── Save to History ──────────────────────────────
    st.session_state.history.append({
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "breed": top_breed_display,
        "confidence": f"{top_confidence:.1f}%",
        "image": img
    })
    if len(st.session_state.history) > 5:
        st.session_state.history.pop(0)

    # ── Export PDF Button ────────────────────────────
    st.markdown("---")
    st.subheader("📄 Export Result")

    # if st.button("📥 Download Result as PDF"):
    #     from fpdf import FPDF
    #     import tempfile
    #     pdf = FPDF()
    #     pdf.add_page()
    #     pdf.set_font("Arial", "B", 16)
    #     pdf.cell(200, 10, "Cattle Breed Recognition Report", ln=True, align="C")
    #     pdf.set_font("Arial", "", 12)
    #     pdf.cell(200, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    #     pdf.cell(200, 10, f"Predicted Breed: {top_breed_display}", ln=True)
    #     pdf.cell(200, 10, f"Confidence: {top_confidence:.1f}%", ln=True)
    #     pdf.cell(200, 10, f"Info: {breed_info.get(top_breed_key, '')}", ln=True)
    #     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
    #         pdf.output(f.name)
    #         with open(f.name, "rb") as pdf_file:
    #             st.download_button(
    #                 label="📄 Click here to Download PDF",
    #                 data=pdf_file.read(),
    #                 file_name="breed_result.pdf",
    #                 mime="application/pdf"
    #             )

    if st.button("📥 Download Result as PDF"):
        from fpdf import FPDF
        import tempfile

        # Remove emojis from text
        def clean(text):
            return text.encode("latin-1", "ignore").decode("latin-1")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, clean("Cattle Breed Recognition Report"), ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, clean(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"), ln=True)
        pdf.cell(200, 10, clean(f"Predicted Breed: {top_breed_display}"), ln=True)
        pdf.cell(200, 10, clean(f"Confidence: {top_confidence:.1f}%"), ln=True)
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, clean("Breed Information:"), ln=True)
        pdf.set_font("Arial", "", 12)
        info_text = breed_info.get(top_breed_key, "A native Indian cattle/buffalo breed.")
        info_clean = clean(info_text)
        pdf.multi_cell(190, 10, info_clean)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            pdf.output(f.name)
            with open(f.name, "rb") as pdf_file:
                st.download_button(
                    label="📄 Click here to Download PDF",
                    data=pdf_file.read(),
                    file_name="breed_result.pdf",
                    mime="application/pdf"
                )

else:
    st.markdown("### 👆 Upload an image to get started!")
    st.markdown("""
    **Supported Breeds:**
    | Cattle 🐄 | Buffalo 🐃 |
    |---|---|
    | Gir | Murrah |
    | Sahiwal | Nili-Ravi |
    | Ongole | Surti |
    | Kankrej | Jaffarabadi |
    | Tharparkar | |
    """)
    st.markdown("---")
    st.info("👈 Use the **sidebar** to navigate to Breed Info, Compare Images, and History pages!")