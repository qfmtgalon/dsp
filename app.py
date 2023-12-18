import streamlit as st
import tensorflow as tf
import librosa
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Load your trained model
model = tf.keras.models.load_model('model_scratch.h5')

def audio_to_spectrogram(audio_file):
    y, sr = librosa.load(audio_file, sr=None, duration=6.0)
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=256, fmax=8000)
    plt.figure(figsize=(3.2, 3.2))
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=8000)
    plt.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img = Image.open(buf)
    img = img.resize((256, 256))
    return np.array(img)/255.0

def classify_audio(audio):
    prediction = model.predict(np.expand_dims(audio, axis=0))
    return 'Real Voice' if prediction[0][0] > 0.5 else 'AI-Generated Voice'

st.title('Real Voice vs AI-Generated Voice Classifier')

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    processed_audio = audio_to_spectrogram(uploaded_file)
    result = classify_audio(processed_audio)
    st.write(f'The audio is classified as: {result}')
