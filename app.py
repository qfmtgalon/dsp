import streamlit as st

def process_audio_file(uploaded_file):
    # Add your processing logic here
    st.audio(uploaded_file, format='audio/wav')

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
