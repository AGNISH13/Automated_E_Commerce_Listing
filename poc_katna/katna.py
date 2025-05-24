from PIL import Image
import io
import base64
import cv2
from Katna.video import Video
import gzip

class InMemoryWriter:
    def __init__(self):
        self.keyframes = []

    def write(self, file_path, images_numpy):
        for frame in images_numpy:
            print(frame.shape)
            b64_frame = self.numpy_array_to_base64(frame)
            self.keyframes.append(b64_frame)
        
        return self.keyframes

    def numpy_array_to_base64(self, np_image, format="png"):
        success, encoded_image = cv2.imencode(f'.{format.lower()}', np_image)
    
        if not success:
            raise ValueError(f"Failed to encode the image as {format}.")
        
        binary_data = encoded_image.tobytes()
        base64_encoded = base64.b64encode(binary_data).decode("utf-8")
        return base64_encoded
    
    def base64_to_image(self, base64_string):    
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))

        return image

def extract_keyframes(video_path):
    # Initialize video module
    vd = Video()

    # Number of images to be returned
    no_of_frames_to_returned = 20

    print(f"Input video file path = {video_path}")

    # List to store keyframes in memory
    keyframes = []

    # Create an instance of the in-memory writer
    memory_writer = InMemoryWriter()
    print("starting...")
    # Extract keyframes and process data with the in-memory writer
    vd.extract_video_keyframes(
        no_of_frames=no_of_frames_to_returned,
        file_path=video_path,
        writer=memory_writer  # Use the in-memory writer
    )

    # Keyframes are now stored in the `keyframes` list
    print(f"Extracted {len(memory_writer.keyframes)} keyframes.")

    keyframes = (memory_writer.keyframes)
    # print(memory_writer.keyframes)
    return keyframes
# return video_id, dict{keyframes}