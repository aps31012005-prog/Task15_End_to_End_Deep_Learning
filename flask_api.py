from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load trained CIFAR-10 model
MODEL_PATH = "model/cifar10_cnn.keras"
model = load_model(MODEL_PATH)

# CIFAR-10 class names
CLASS_NAMES = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Task 15 CIFAR-10 Deep Learning API is running",
        "endpoint": "/predict",
        "method": "POST"
    })


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    try:
        image_file = request.files["image"]

        # Open and preprocess image
        image = Image.open(image_file).convert("RGB")
        image = image.resize((32, 32))

        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Model prediction
        predictions = model.predict(image_array, verbose=0)

        predicted_index = int(np.argmax(predictions[0]))
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = float(np.max(predictions[0]) * 100)

        return jsonify({
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )