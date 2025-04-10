import time
from datetime import datetime
import os
import streamlit as st

from pipeline import pipeline
from crud import video, transcripts, keyframes, keyframe_classes, final_class
from poc_whisper.whisper import transcribe_audio_from_bytes  # Importing Whisper processing

'''
VIDEO UPLOAD PAGE ---------------------------------------------
Choose whether to upload file or input file path
Create a duplicate of the file in the uploads folder
If the file already exists, remove it and create a new one
'''

# st.set_page_config(page_title="Video Upload", page_icon="📹", layout="wide")
# st.write("""## Uploading video""") 

uploaded_file = st.file_uploader("choose videos", type=["mp4"], accept_multiple_files=True, label_visibility="hidden")
if uploaded_file:
    session_start_time = str(datetime.now())
    if 'session_start_time' not in st.session_state:
        st.session_state['session_start_time'] = session_start_time.replace(" ", "_").replace(":", "-").replace(".", "-")

    for file in uploaded_file:
        # video_display = st.video(uploaded_file, format="video/mp4")
        name = file.name
        file_path = "stlit/uploads/"+name+"upload_at_"+st.session_state['session_start_time']+".mp4"
        if os.path.isfile(file_path):
            os.remove(file_path)
        with open(file_path, "wb") as write_file:
            write_file.write(uploaded_file.getvalue())

    # RUN POC STEPS ---------------------------------------------

    video_path_list = []
    for file in os.path("stlit/uploads/"):
        if file.endswith(st.session_state["session_start_time"]+".mp4"):
            video_path_list.append(file)
    
    # create video id and send to database
    steps = pipeline(video_path_list)
    video_id_list = steps.create_video_obj()

    if 'video_id' not in st.session_state:
        st.session_state['video_id'] = video_id_list # update session state with list of video ids

    transcript_list = steps(file_path).run_pipeline()

