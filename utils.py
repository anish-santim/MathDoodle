import base64
import re
import cv2
import numpy as np
from PIL import Image, ImageFilter

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def remove_special_chars(text):
    formatted = re.sub(r'^\$\$|\$\$$', '', text)  
    formatted = re.sub(r'\\\[|\]', '', formatted)
    
    replacements = {
        r'\\frac{([^}]+)}{([^}]+)}': r'(\1/\2)',
        r'\\sqrt{([^}]+)}': r'√(\1)',
        r'\\sin': 'sin', r'\\cos': 'cos', r'\\tan': 'tan',
        r'\\int_{([^}]+)}^{([^}]+)}': r'∫_{\1}^{\2}',
        r'\\int': '∫',
        r'\\sum': '∑', r'\\prod': '∏',
        r'\\cup': '∪', r'\\cap': '∩',
        r'\\left\(': '(', r'\\right\)': ')',
        r'\\begin{bmatrix}': '[', r'\\end{bmatrix}': ']',
        r'\\infty': '∞',
        r'\\rightarrow': '→', r'\\to': '→',
        r'\\geq': '≥', r'\\leq': '≤', r'\\neq': '≠',
        r'\\cdot': '·',
        r'\\, dx': ' dx',
        r'\$': ''
    }

    for latex, plain in replacements.items():
        formatted = re.sub(latex, plain, formatted)

    formatted = formatted.rstrip('\\').strip()

    return formatted

def preprocess_image(image):
    gray_image = image.convert("L")
    np_image = np.array(gray_image)
    _, threshold_image = cv2.threshold(np_image,  0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    threshold_image_pil = Image.fromarray(threshold_image)
    threshold_image_pil = threshold_image_pil.filter(ImageFilter.MedianFilter(3))
    return threshold_image_pil
