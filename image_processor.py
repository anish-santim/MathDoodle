import os
import secrets
from PIL import Image
from utils import preprocess_image
from ai_handler import generate_response_from_ai

def process_image(image):
    image = preprocess_image(image)
    image_dir = "images"
    os.makedirs(image_dir, exist_ok=True)
    file_name = f"tmp{secrets.token_hex(8)}.png"
    image_path = os.path.join(image_dir, file_name)
    image.save(image_path)

    response = generate_response_from_ai(image_path)
    os.remove(image_path)

    return response
