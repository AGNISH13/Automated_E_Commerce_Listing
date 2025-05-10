import streamlit as st

class Display:
    def __init__(self, *args, **kwargs):
        pass

    def display1(self):
        st.write(st.session_state['flag1_content'])

    def display2(self):
        st.write(st.session_state['flag2_content']) 

    def close(self):
        pass