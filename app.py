import streamlit as st
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def process_audio_file(uploaded_file):
    # Convert uploaded file to an audio segment
    audio_segment = AudioSegment.from_file(uploaded_file)
    
    # Convert audio_segment to numpy array
    samples = np.array(audio_segment.get_array_of_samples())

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(samples)
    plt.title('Audio Waveform')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.grid()

    # Convert plot to a PNG and display it using Streamlit
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    st.image(buf, caption='Waveform of the uploaded audio file')

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
