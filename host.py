import time
from datetime import datetime
import os
import streamlit as st
from utils.video_path import get_video_path

from crud import video, transcripts, keyframes, keyframe_classes, final_class
from poc_whisper.whisper import transcribe_audio_from_bytes  # Importing Whisper processing
# from poc_katna.katna import extract_keyframes    # Importing Katna processing
# from poc_filtering.filtering import filter_images  # Importing Filtering
# from poc_yolo.yolo2 import detect_objects  # Importing YOLO detection

# other functions
def get_video_path():
    return file_path

def create_video_obj():
    videoobj = video()
    video_id = videoobj.create(video_link=st.session_state['file_path'])
    return None

def whisper():
    transcript = transcribe_audio_from_bytes(st.session_state['file_path']) #  return audio transcript -> string
    transcriptobj = transcripts()
    transcipt_id = transcriptobj.create(video_id=st.session_state['video_id'],transcript=transcript)
    return transcript

# VIDEO UPLOAD PAGE ---------------------------------------------
# Choose whether to upload file or input file path
# Create a duplicate of the file in the uploads folder
# If the file already exists, remove it and create a new one

# st.set_page_config(page_title="Video Upload", page_icon="📹", layout="wide")
st.write("""## Uploading video""") 

session_start_time = str(datetime.now())
if 'session_start_time' not in st.session_state:
    st.session_state['session_start_time'] = session_start_time

t = st.session_state['session_start_time'].replace(" ", "_").replace(":", "-").replace(".", "-")
file_path = "stlit/uploads/video_at_"+t+".mp4"

if 'file_path' not in st.session_state:
    st.session_state['file_path'] = file_path

if os.path.isfile(file_path):
    os.remove(file_path)

uploaded_file = st.file_uploader("Upload video", type=["mp4"])
if uploaded_file:
    video_display = st.video(uploaded_file, format="video/mp4")
    with open(file_path, "wb") as write_file:
        write_file.write(uploaded_file.getvalue())

    # RUN POC STEPS ---------------------------------------------

    # create video id and send to database
    if 'video_id' not in st.session_state:
        st.session_state['video_id'] = create_video_obj()

    # run whisper and display transcript
    if 'transcript' not in st.session_state:
        st.session_state['transcript'] = whisper()
    
    if os.path.isfile(file_path):
        st.write("""## Transcript""") 
        st.write("Transcribing audio with Whisper...")
        st.write(st.session_state['transcript'])
