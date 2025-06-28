Audio Emotion Recognition App – Built with TensorFlow + Gradio 
I'm thrilled to share my latest end-to-end AI project: an Audio Emotion Recognition web app that predicts human emotions from voice samples 🎙️—whether it's anger 😠, joy 😊, or surprise 😲!

What This Project Is About?

I built a machine learning model that listens to your spoken audio and classifies it into one of 8 human emotions:
angry, calm, disgust, fearful, happy, neutral, sad, and surprised.
It uses deep learning and signal processing techniques to analyze the speech and infer the underlying emotion. The final result? A simple, interactive web app anyone can try online!

Try it here: https://huggingface.co/spaces/nairsanjay20/Audio-Emotion_Recognition_v2

What I Did
✔ Built a Convolutional Neural Network (CNN) for classifying spectrograms
✔ Extracted audio features using MFCCs (Mel-frequency cepstral coefficients)
✔ Integrated Gradio for UI and real-time microphone inputs
✔ Enabled confidence scores + emotion emojis for user clarity
✔ Deployed using Hugging Face Spaces for free, GPU-enabled hosting

Key Takeaways

🔸 Learned how to convert raw audio to mel spectrograms
🔸 Understood the real-world challenges of emotion detection in speech
🔸 Integrated audio processing tools like PyDub, librosa, and Gradio
🔸 Understood how to deploy apps on Hugging Face Spaces with version control

Mistakes I Made

❌ Initially tried pushing the model folder to GitHub which led to LFS issues
❌ Faced inaccurate predictions due to noisy microphone inputs
❌ Struggled with Hugging Face’s gradio deploy and large file uploads
✅ Learned how to manually manage LFS + upload directly to resolve it all!

⚙️ Tools & Technologies Used
TensorFlow / Keras
Gradio
PyDub + librosa
NumPy + Pandas
Hugging Face Spaces
Git + Git LFS
VS Code, PowerShell

Future Scope
- Train on a larger emotional voice dataset (e.g., RAVDESS + IEMOCAP)
- Improve real-time accuracy using noise filtering & augmentation (Still WIP)
- Deploy as a mobile/web app using Flask or Streamlit
- Add waveform & spectrogram visualizations on UI
- Dockerize and deploy to Render or Hugging Face with CI/CD

If you're interested in voice-based AI, ML deployment, or building fun real-world projects, let’s connect! I’m open to collaborations, feedback.
