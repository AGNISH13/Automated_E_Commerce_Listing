import sys
import os
import streamlit as st
from datetime import datetime

from pipeline import Pipeline
from stlit.dummy_display import Display

def page():
    st.set_page_config(page_title="SAM", page_icon="📹", layout="wide")
    if 'pipeline' not in st.session_state:
        st.session_state['pipeline'] = Pipeline()
    if 'display' not in st.session_state:
        st.session_state['display'] = Display()

    header = st.container()
    body = st.container()

    with header:
        st.write("# Running dummy pipelines")
        file = st.file_uploader("choose videos", type=["mp4"], accept_multiple_files=False, label_visibility="hidden")

    if file:
        session_start_time = str(datetime.now())
        if 'session_start_time' not in st.session_state:
            st.session_state['session_start_time'] = session_start_time.replace(" ", "_").replace(":", "-").replace(".", "-")
        name = file.name
        file_path = "stlit/uploads/"+name+"upload_at_"+st.session_state['session_start_time']+".mp4"
        if os.path.isfile(file_path):
            os.remove(file_path)
        with open(file_path, "wb") as write_file:
            write_file.write(file.getvalue())
        
        st.session_state['pipeline'].setup(file_path)
        st.button("reset pipeline", key="reset_pipeline", type="secondary", on_click=st.session_state['pipeline'].reset) #, args=(test,))
        with body:
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("The uploaded video")
                st.video(file, format="video/mp4")
            # file_data = file.getvalue()
            with col2:
                # st.write("Other data will be displayed here")
                # st.session_state['pipeline'].step=2
                # st.session_state['pipeline'].auto_run()
                # if st.session_state['pipeline'].flag_katna:
                #     binaries = st.session_state['pipeline'].katna_keyframes
                #     st.session_state['display'].display_bnr_frames(binaries)
                #     st.session_state['pipeline'].flag_katna = False
                st.session_state['pipeline'].auto_run()
                while st.session_state['pipeline'].step != -1:
                    st.session_state['pipeline'].auto_run()
                    if st.session_state['pipeline'].flag_transcript:
                        st.session_state['display'].display_transcript()
                        st.session_state['pipeline'].flag_transcript = False

                    if st.session_state['pipeline'].flag_katna:
                        binaries = st.session_state['pipeline'].katna_keyframes
                        st.session_state['display'].display_bnr_frames(binaries)
                        st.session_state['pipeline'].flag_katna = False

                    if st.session_state['pipeline'].flag_description:
                        st.session_state['display'].display_description()
                        st.session_state['pipeline'].flag_description = False

                if st.session_state['pipeline'].step == -1:
                    st.write("Pipeline has ended")
                    # st.session_state['pipeline'].reset()
                    st.session_state['display'].close()
            st.write("not in column")

page()