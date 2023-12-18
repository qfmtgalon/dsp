import streamlit as st
from pydub import AudioSegment
from io import BytesIO

def process_audio(audio_file):
    # Convert audio file to bytes
    audio_bytes = audio_file.read()

    # Create an AudioSegment object
    audio = AudioSegment.from_file(BytesIO(audio_bytes))

    return audio

def main():
    st.title("Audio Player App")

    # Upload audio file through Streamlit
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        st.audio(process_audio(uploaded_file), format='audio/wav')

if __name__ == "__main__":
    main()
