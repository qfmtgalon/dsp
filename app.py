import streamlit as st
import tensorflow as tf
import librosa
import numpy as np
import cv2


# Load your trained model
model = tf.keras.models.load_model('model_scratch.h5')

# Maximum duration for processing
MAX_DURATION = 6.0
def preprocess_audio(file):
    # Load audio file
    y, sr = librosa.load(file, sr=None, duration=MAX_DURATION)

    # Convert audio signal to spectrogram (adjust parameters as needed)
    spectrogram = librosa.feature.melspectrogram(y, sr=sr, n_fft=2048, hop_length=512)
    spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

    # Resize the spectrogram to match the model's input shape
    resized_spectrogram = cv2.resize(spectrogram, (256, 256), interpolation=cv2.INTER_NEAREST)

    # Expand dimensions to create a batch of size 1
    processed_audio = np.expand_dims(resized_spectrogram, axis=-1)
    processed_audio = np.expand_dims(processed_audio, axis=0)

    return processed_audio


def classify_audio(audio):
    # Use your model to classify the audio
    prediction = model.predict(audio)
    return 'Real Voice' if prediction[0][0] > 0.5 else 'AI-Generated Voice'

st.title('Real Voice vs AI-Generated Voice Classifier')

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Process the audio file
    processed_audio = preprocess_audio(uploaded_file)

    # Classify the audio
    result = classify_audio(processed_audio)

    # Display the result
    st.write(f'The audio is classified as: {result}')
