import streamlit as st
from tempfile import NamedTemporaryFile
import librosa


def validate_mp3(uploaded_file):
    try:
        audio, sr = librosa.load(uploaded_file, sr=None)
        return True
    except:
        return False


st.title("MP3 Player")

uploaded_file = st.file_uploader("Upload your MP3 audio", type=["mp3"])

if uploaded_file:
    # Validate if it's actually an MP3 file
    if not validate_mp3(uploaded_file):
        st.error("Please upload a valid MP3 file.")
    else:
        with NamedTemporaryFile(suffix=".mp3") as temp:
            temp.write(uploaded_file.read())
            temp.seek(0)
            st.audio(temp.name, autoplay=False)
            st.button("Play", on_click=lambda: st.session_state.play_audio)
            if st.session_state.get("play_audio", False):
                st.audio(temp.name, format="audio/mpeg", autoplay=True)
                del st.session_state.play_audio

else:
    st.write("Please upload an MP3 file to play.")


