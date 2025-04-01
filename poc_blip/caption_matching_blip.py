# Install required libraries
# !pip install torch torchvision transformers accelerate datasets huggingface-hub
# !pip install opencv-python-headless

# Import necessary libraries
import os
from PIL import Image
import io
from transformers import BlipProcessor, BlipForConditionalGeneration
import cv2
import base64

# Step 1: Inputs from Redis
# required_objects = []  # User input
# binaries = []

def blip_filter(filtered_keyframes, required_objects): # [{id: bnr},..], [str,..] -> [{id: bnr},..]
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    matched_img = [] # {keyframes_id: keyframe_binary}
    for base64_image in filtered_keyframes:
        binary = base64_image["keyframe"]
        binary = base64.b64decode(binary)

        image_stream = io.BytesIO(binary)
        image = Image.open(image_stream).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        print(caption)

        if any(obj.lower() in caption.lower() for obj in required_objects):
            matched_img.append(base64_image)

    return matched_img

# Step 3: Process YOLO keyframes and filter them
def filter_keyframes(images, required_objects): # array[binaries], array[string] -> dict{binary: caption}, dict{binary: caption}
    # Load the BLIP model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    d = dict()
    matched_img = []
    for image in images:
        binary = base64.b64decode(image)
        image_stream = io.BytesIO(binary)
        image = Image.open(image_stream).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        print(f"Caption for {image}: {caption}")
        d[image] = caption

        if any(obj.lower() in caption.lower() for obj in required_objects):
            matched_img.append(image)
    
    # d = dictionary of all keyframe: caption
    # matched_img = dictionary of matched keyframe: caption

    return d, matched_img

        
# dic, matches = filter_keyframes(binaries, required_objects)


