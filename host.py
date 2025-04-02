import time
import datetime
import os
import streamlit as st
from utils.video_path import get_video_path

st.write("Reading the video") 

t = str(time.time())
timestamp = datetime.fromtimestamp(t)
FILE_OUTPUT = "uploads/video_at_"+t+".mp4"

if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

uploaded_file = st.file_uploader("Upload video", type=["mp4"])
if uploaded_file:
    video_display = st.video(uploaded_file, format="video/mp4")
    with open(FILE_OUTPUT, "wb") as write_file:
        write_file.write(uploaded_file.getvalue())

def get_video_path():
    return FILE_OUTPUT