import streamlit as st
import tensorflow as tf
import librosa
import numpy as np

# Load your trained model
model = tf.keras.models.load_model('model_scratch.h5')

# Maximum duration for processing
MAX_DURATION = 6.0

def preprocess_audio(file):
    # Load audio file
    y, sr = librosa.load(file, sr=None, duration=MAX_DURATION)
    
    # Add your preprocessing steps here
    # For example, you might need to extract features or reshape the data
    
    # Ensure the processed audio has the same shape as expected by the model
    processed_audio = np.expand_dims(y, axis=0)
    
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
