import streamlit as st
import base64

class Display:
    def __init__(self, *args, **kwargs):
        pass

    def display_transcript(self):
        st.write(st.session_state['pipeline'].transcript)

    def display_description(self):
        print(f"inside display - {st.session_state['pipeline'].transcript}")
        st.write(st.session_state['pipeline'].description)

    def display_bnr_frames(self, binaries):
        byte_data = []
        if not isinstance(binaries, list):
            binaries = [binaries]
        for bnr in binaries:
            decoded = base64.b64decode(bnr)
            byte_data.append(bytes(decoded))            
        st.image(byte_data)

    def close(self):
        pass