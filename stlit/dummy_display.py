import streamlit as st

class Display:
    def __init__(self, *args, **kwargs):
        pass

    def display_transcript(self):
        st.write(st.session_state['pipeline'].transcript)

    def display_description(self):
        st.write(st.session_state['pipeline'].description)

    def close(self):
        pass