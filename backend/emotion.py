import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model

# Path management for safety
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "emotion_model.h5")

# Load model once
try:
    model = load_model(MODEL_PATH, compile=False)
    print("Emotion Model Loaded Successfully")
except Exception as e:
    print(f"Model Load Error: {e}")

emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def predict_emotion(image: np.ndarray):
    target_size = (64, 64)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

    if len(faces) == 0:
        face_roi = cv2.resize(gray, target_size)
    else:
        x, y, w, h = faces[0]
        face_roi = cv2.resize(gray[y:y+h, x:x+w], target_size)

    face_normalized = face_roi.astype("float32") / 255.0
    face_final = face_normalized.reshape(1, 64, 64, 1)
    
    prediction = model.predict(face_final, verbose=0)
    idx = np.argmax(prediction[0])
    
    return {
        "label": emotion_labels[idx],
        "confidence": float(prediction[0][idx])
    }