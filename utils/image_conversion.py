import io
import base64
from PIL import Image
from io import BytesIO

# takes a base64 encoded image and return a PIL image
def base64_to_image(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))
    return image

# take a list or a single PIL image and return a list of base64 encoded image
def image_to_base64(image):
    if isinstance(image, list):
        images = image
    else:
        images = [image]
    encoded = []
    for element in enumerate(images):
        buffered = BytesIO()
        element.save(buffered, format="PNG")
        buffered.seek(0)
        img_byte = buffered.getvalue()
        img_str = base64.b64encode(img_byte).decode("utf-8")
        encoded.append(img_str)
    return encoded