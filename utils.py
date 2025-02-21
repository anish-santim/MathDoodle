import base64
import re
import cv2
import numpy as np
from PIL import Image

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def remove_special_chars(text):
    char_to_remove = '\\[]{}'
    pattern = f"[{re.escape(char_to_remove)}]"
    return re.sub(pattern, "", text).replace("boxed", "")

def preprocess_image(image):
    image = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(thresh)
