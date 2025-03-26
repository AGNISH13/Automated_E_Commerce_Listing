# import absl.logging
# absl.logging.set_verbosity(absl.logging.INFO)

import cv2
import numpy as np
import mediapipe as mp


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

# Load the image
image_path = '/home/agnish_gg/amazon_listing_sam/poc_filtering/no_middle_finger.jpeg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Process the image and detect hands
results = hands.process(image_rgb)

# Function to detect middle finger
def is_middle_finger_up(hand_landmarks):
    # Landmarks for the middle finger
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    middle_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    
    # Check if the middle finger is up
    if middle_finger_tip.y < middle_finger_pip.y < middle_finger_mcp.y:
        return True
    return False

# Draw landmarks and check for middle finger
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        if is_middle_finger_up(hand_landmarks):
            print("Middle finger detected!")

        else :
            print("Middle finger not detected!")

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()