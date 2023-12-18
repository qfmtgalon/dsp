import streamlit as st
from io import BytesIO
from pydub import AudioSegment

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write.audio(audio_data, format=audio_format)
        play_audio = True

        # Check if the file type is supported
        if uploaded_file.type == "audio/mp3" or uploaded_file.type == "audio/wav" or uploaded_file.type == "audio/m4a":
            st.audio(uploaded_file.read(), format=uploaded_file.type)

        else:
            st.write("Uploaded file type not supported. Please upload an MP3 or WAV file.")

if __name__ == "__main__":
    main()
