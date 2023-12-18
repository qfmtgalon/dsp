import streamlit as st
import librosa
import matplotlib.pyplot as plt
import numpy as np

def process_audio_file(uploaded_file):
    # Add your processing logic here
    st.audio(uploaded_file, format='audio/wav')

    # Load audio using librosa
    y, sr = librosa.load(uploaded_file)

    # Plot waveform
    plt.figure(figsize=(8, 4))
    plt.title('Waveform Visualization')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(np.arange(len(y)) / sr, y)
    st.pyplot()

def main():
    st.title('Audio File Uploader and Waveform Visualizer')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
