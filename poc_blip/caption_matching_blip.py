# Install required libraries
# !pip install torch torchvision transformers accelerate datasets huggingface-hub
# !pip install opencv-python-headless

# Import necessary libraries
import os
import torch
from PIL import Image
import io
from transformers import BlipProcessor, BlipForConditionalGeneration
import cv2

# Step 1: Inputs from Redis
# required_objects = []  # User input
# binaries = []

# Step 2: Load the BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Step 3: Process YOLO keyframes and filter them
def filter_keyframes(binaries, required_objects):
    d = dict()
    matched_bnr = []
    for binary in binaries:
        image_stream = io.BytesIO(binary)
        image = Image.open(image_stream).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        print(f"Caption for {binary}: {caption}")
        d[binary] = caption

        if any(obj.lower() in caption.lower() for obj in required_objects):
            matched_bnr.append(binary)

    return d, matched_bnr
        
# dic, matches = filter_keyframes(binaries, required_objects)
