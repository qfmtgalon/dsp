import streamlit as st

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Check if the file type is supported
        if uploaded_file.type == "audio/mp3" or uploaded_file.type == "audio/wav" or uploaded_file.type == "audio/m4a":
            # Display the audio player for playback
            st.audio(uploaded_file, format=uploaded_file.type)

        else:
            st.write("Uploaded file type not supported. Please upload an MP3, WAV, or M4A file.")

if __name__ == "__main__":
    main()
