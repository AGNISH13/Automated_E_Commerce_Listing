import os
from PIL import Image
import numpy as np
import cv2
import mediapipe as mp
from nudenet import NudeDetector
import base64
from io import BytesIO

# Initialize NudeNet Detector
detector = NudeDetector()
explicit = ["BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "ANUS_EXPOSED",
            "MALE_GENITALIA_EXPOSED"]

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
drawing_utils = mp.solutions.drawing_utils

# Function to detect middle finger
def is_middle_finger_up(hand_landmarks):
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    middle_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

    return middle_finger_tip.y < middle_finger_pip.y < middle_finger_mcp.y


# Function to process images
def filter_images(base64_images):
    binary_images = [base64.b64decode(img) for img in base64_images]
    filtered_images = []

    for i,binary_image in enumerate(binary_images):
        try:

            # Detect vulgar content using NudeNet
            detections = detector.detect(binary_image)
            flag=0
            
            for detection in detections:
                if detection['class'] in explicit:
                    print(f"Vulgar content detected")
                    flag=1
                    break
            if flag==1:
                continue
            # Load and process the image for middle finger detection
            np_arr = np.frombuffer(binary_image, dtype=np.uint8)
            image_rgb = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            results = hands.process(image_rgb)

            middle_finger_detected = False
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    drawing_utils.draw_landmarks(image_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    if is_middle_finger_up(hand_landmarks):
                        middle_finger_detected = True
                        flag=1
                        break

            if middle_finger_detected:
                print(f"Middle finger detected")
                continue

            if flag==1:
                continue

            # If no vulgar content or middle finger detected, add to filtered list
            filtered_images.append(base64_images[i])

        except Exception as e:
            print(f"Error processing : {e}") # {image_path}

    return filtered_images      # -> list[base64]

# Example usage
# image_directory = "/home/agnish_gg/amazon_listing_sam/poc_filtering/Images"
# image_paths = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
# filtered_images = filter_images(image_paths)

# print("Filtered images:", filtered_images)