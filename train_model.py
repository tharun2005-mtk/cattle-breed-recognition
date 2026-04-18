# Training script
import matplotlib
matplotlib.use('Agg')  # Saves plot without opening popup window
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
import os

# ── Suppress warnings ────────────────────────────────
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# ── Config ───────────────────────────────────────────
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 20
DATASET_DIR = "dataset/train"

print("📁 Loading dataset...")

# ── Data Augmentation ────────────────────────────────
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    rotation_range=25,
    width_shift_range=0.1,
    height_shift_range=0.1,
    brightness_range=[0.8, 1.2],
    shear_range=0.1
)

train_data = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    subset="training",
    class_mode="categorical"
)

val_data = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    subset="validation",
    class_mode="categorical",
    shuffle=False
)

num_classes = len(train_data.class_indices)
print(f"✅ Found {num_classes} breeds!")
print(f"📊 Training samples : {train_data.samples}")
print(f"📊 Validation samples: {val_data.samples}")
print("-" * 40)

# ── Build Model ──────────────────────────────────────
print("🧠 Building model...")

base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)
base_model.trainable = False  # Freeze pretrained layers

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation="relu")(x)
x = Dropout(0.4)(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)
output = Dense(num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("✅ Model built successfully!")
print(f"📐 Total parameters: {model.count_params():,}")
print("-" * 40)

# ── Callbacks ────────────────────────────────────────
os.makedirs("model", exist_ok=True)

callbacks = [
    EarlyStopping(
        monitor="val_accuracy",
        patience=5,
        restore_best_weights=True,
        verbose=1
    ),
    ModelCheckpoint(
        "model/best_model.h5",
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    )
]

# ── Train ────────────────────────────────────────────
print("🚀 Starting training...")
print("-" * 40)

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS,
    callbacks=callbacks
)

# ── Save Final Model ─────────────────────────────────
model.save("model/breed_model.h5")

# Save class names
import json
class_names = {v: k for k, v in train_data.class_indices.items()}
with open("model/class_names.json", "w") as f:
    json.dump(class_names, f)

print("-" * 40)
print("✅ Model saved → model/breed_model.h5")
print("✅ Class names saved → model/class_names.json")

# ── Plot Results ─────────────────────────────────────
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Train Accuracy", color="blue")
plt.plot(history.history["val_accuracy"], label="Val Accuracy", color="orange")
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Train Loss", color="blue")
plt.plot(history.history["val_loss"], label="Val Loss", color="orange")
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("model/training_plot.png")
plt.show()
print("✅ Training plot saved → model/training_plot.png")