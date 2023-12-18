import streamlit as st
from io import BytesIO
from pydub import AudioSegment

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Check if the file type is supported
        if uploaded_file.type in ["audio/mp3", "audio/wav", "audio/m4a"]:
            # Convert the uploaded file to bytes
            file_bytes = uploaded_file.getvalue()
            
            # Display the audio player
            st.audio(file_bytes, format='audio/mp3')

        else:
            st.write("Uploaded file type not supported. Please upload an MP3, WAV, or M4A file.")

if __name__ == "__main__":
    main() 
