import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from utils import extract_features
from pydub import AudioSegment
import os
import uuid

emotion_classes = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

model = load_model("model/audio_emotion_model.h5")

def predict_emotion(audio):
    # Save input temporarily
    temp_filename = f"{uuid.uuid4()}.wav"
    audio.export(temp_filename, format="wav")

    # Extract features
    features = extract_features(temp_filename)
    features = np.expand_dims(features, axis=0)

    # Predict
    prediction = model.predict(features)[0]
    predicted_label = emotion_classes[np.argmax(prediction)]
    confidence_scores = {emotion_classes[i]: float(f"{p:.3f}") for i, p in enumerate(prediction)}

    os.remove(temp_filename)

    return f"🎯 Emotion: {predicted_label}", confidence_scores

interface = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Audio(type="auto", label="Upload Audio (.wav or .mp3)"),
    outputs=[
        gr.Text(label="Predicted Emotion"),
        gr.Label(label="Confidence Scores")
    ],
    title="🎧 Audio Emotion Recognition"
)

interface.launch()
