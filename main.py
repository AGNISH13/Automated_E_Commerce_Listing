import argparse
import os
import subprocess
import cv2
import numpy as np

from utils.video_path import get_video_path
from poc_whisper.whisper import transcribe_audio_from_bytes  # Importing Whisper processing
from poc_katna.katna import extract_keyframes    # Importing Katna processing
from poc_filtering.filtering import filter_images  # Importing Filtering
from poc_yolo.yolo2 import detect_objects  # Importing YOLO detection
# from blip import generate_captions  # Importing BLIP captioning
# from gemini import classify_and_confirm  # Importing Gemini classification

def main():

    video_path = get_video_path()

    if not os.path.exists(video_path):
        print("Error: Video file not found.")
        return

    print("Processing audio with Whisper...")
    transcript = transcribe_audio_from_bytes(video_path) #  return audio transcript -> string

    print("Extracting keyframes using Katna...")
    keyframes = extract_keyframes(video_path)            # return keyframes -> list[base64]

    print("Applying profanity filter...")
    filtered_keyframes = filter_images(keyframes)        # return filtered_keyframes -> list[base64] 

    # store in database

    print("Running YOLO object detection...")
    # detected_keyframes, class_ids = detect_objects(filtered_keyframes)
    class_ids = detect_objects(filtered_keyframes)
    
    # print("Processing detected objects with Gemini AI...")
    # confirmed_product, final_prompt = classify_and_confirm(class_ids, transcript)

    # if confirmed_product:
    #     print("Generating captions with BLIP...")
    #     final_caption = generate_captions(confirmed_product)

    #     print("Final Output:")
    #     print(f"Confirmed Product: {confirmed_product}")
    #     print(f"Final Caption: {final_caption}")
    # else:
    #     print("No result found. Prompt updated for further refinement.")

if __name__ == "__main__":
    main()