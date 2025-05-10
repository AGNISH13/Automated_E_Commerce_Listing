import streamlit as st

class Pipeline:
    def __init__(self):
        self.step = 0
        st.session_state['flag1'] = False
        st.session_state['flag2'] = False

    def run(self):
        self.step += 1
        if self.step>2:
            st.session_state['flag1']==True
            st.session_state['flag1_content'] = "flag1_content"
        if self.step>3:
            st.session_state['flag2']==True
            st.session_state['flag2_content'] = "flag2_content"
        return self.step

    def reset(self):
        self.step = 0
        return self.step
    
    def end(self):
        self.step = -1
        return self.step