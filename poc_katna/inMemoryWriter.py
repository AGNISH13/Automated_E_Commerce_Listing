from PIL import Image
import io
import base64
import cv2

class InMemoryWriter:
    def __init__(self):
        self.keyframes = []

    def write(self,images_numpy):
        for frame in images_numpy:
            print(frame.shape)
            b64_frame = self.numpy_array_to_base64(frame)
            self.keyframes.append(b64_frame)
        
        return self.keyframes

    def numpy_array_to_base64(self,np_image, format="png"):
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
