from flask import Flask, request, jsonify
import numpy as np
import os
from tensorflow.keras.models import load_model
from utils import extract_features
from pydub import AudioSegment
import uuid
import logging

app = Flask(__name__)

# Load model
MODEL_PATH = 'model/audio_emotion_model.h5'
model = load_model(r"H:/INeuron/Datasets/Deep Learning/audio_emotion_api/model/audio_emotion_model.h5")


# Emotion labels
emotion_classes = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# Set up logging
logging.basicConfig(filename='api_logs.txt', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/')
def home():
    return "🎧 Audio Emotion Recognition API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_ext = file.filename.split('.')[-1].lower()
    temp_filename = f"{uuid.uuid4()}.wav"
    
    try:
        if file_ext == 'mp3':
            temp_mp3 = f"{uuid.uuid4()}.mp3"
            file.save(temp_mp3)
            sound = AudioSegment.from_mp3(temp_mp3)
            sound.export(temp_filename, format="wav")
            os.remove(temp_mp3)
        else:
            file.save(temp_filename)

        # Extract features and predict
        features = extract_features(temp_filename)
        features = np.expand_dims(features, axis=0)
        prediction = model.predict(features)[0]
        predicted_label = emotion_classes[np.argmax(prediction)]
        confidence_scores = {emotion_classes[i]: float(f"{p:.3f}") for i, p in enumerate(prediction)}

        # Log the request
        logging.info(f"Predicted: {predicted_label} | Confidence: {confidence_scores}")

        return jsonify({
            'predicted_emotion': predicted_label,
            'confidence_scores': confidence_scores
        })

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

# Start the app (only needed if using `python app.py`)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns a PORT env var
    app.run(host="0.0.0.0", port=port)

