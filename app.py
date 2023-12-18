import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

# Function to process the uploaded audio file
def process_audio_file(uploaded_file):
    st.audio(uploaded_file, format='audio/wav')

    # Load audio using librosa
    y, sr = librosa.load(uploaded_file, sr=None)

    # Plot waveform
    st.header('Waveform Visualization')
    waveform_chart = st.pyplot(plt.figure(figsize=(8, 4)))
    plt.plot(np.arange(len(y)) / sr, y)
    waveform_chart.pyplot()

    # Create and display mel spectrogram
    st.header('Mel Spectrogram')
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

    mel_spec_chart = st.pyplot(plt.figure(figsize=(10, 4)))
    librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    mel_spec_chart.pyplot()

# Main function for Streamlit web app
def main():
    st.set_page_config(layout="wide", page_title='Audio Analysis App', page_icon='🔊')
    st.title('Classifying Real vs. AI-Generated Voices: A Deep Learning Approach Using Mel Spectrogram Analysis')
    st.markdown('## Analyze Audio Files')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
