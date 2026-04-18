# Evaluation script
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

print("📂 Loading model...")
model = tf.keras.models.load_model("model/best_model.h5")

# ── Load Validation Data ─────────────────────────────
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

val_data = datagen.flow_from_directory(
    "dataset/train",
    target_size=(224, 224),
    batch_size=16,
    subset="validation",
    class_mode="categorical",
    shuffle=False
)

labels = list(val_data.class_indices.keys())
labels_clean = [l.replace("_India", "").replace("_", " ") for l in labels]

print("🔍 Running predictions...")
y_pred_probs = model.predict(val_data)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = val_data.classes

# ── Classification Report ────────────────────────────
print("\n" + "="*50)
print("📋 CLASSIFICATION REPORT")
print("="*50)
print(classification_report(y_true, y_pred, target_names=labels_clean))

# ── Confusion Matrix ─────────────────────────────────
print("📊 Saving confusion matrix...")
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(12, 8))
sns.heatmap(
    cm, annot=True, fmt="d",
    xticklabels=labels_clean,
    yticklabels=labels_clean,
    cmap="Blues"
)
plt.title("Confusion Matrix — Cattle & Buffalo Breed Recognition", fontsize=14)
plt.ylabel("Actual Breed")
plt.xlabel("Predicted Breed")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("model/confusion_matrix.png", dpi=150)
plt.show()

print("✅ Confusion matrix saved → model/confusion_matrix.png")

# ── Overall Summary ──────────────────────────────────
correct = np.sum(y_pred == y_true)
total = len(y_true)
print("\n" + "="*50)
print(f"✅ Correct Predictions : {correct}/{total}")
print(f"📈 Overall Accuracy    : {correct/total*100:.2f}%")
print("="*50)