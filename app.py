import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Disable PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

def process_audio_file(uploaded_file):
    # Add your processing logic here
    st.audio(uploaded_file, format='audio/wav')

    # Load audio using librosa
    y, sr = librosa.load(uploaded_file)

    # Plot waveform
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.title('Waveform Visualization')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(np.arange(len(y)) / sr, y)

    # Compute mel spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y, sr=sr)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

    # Plot mel spectrogram
    plt.subplot(1, 2, 2)
    librosa.display.specshow(mel_spectrogram_db, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel Spectrogram')
    plt.xlabel('Time')
    plt.ylabel('Mel Frequency')
    
    st.pyplot()

def main():
    st.title('Audio File Uploader and Waveform/Mel Spectrogram Visualizer')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
