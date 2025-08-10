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
