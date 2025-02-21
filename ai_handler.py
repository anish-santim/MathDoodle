import os
from dotenv import load_dotenv
from groq import Groq
from utils import encode_image, remove_special_chars

load_dotenv()
llm = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response_from_ai(image_path):
    base64_image = encode_image(image_path)
    messages = [{
        'role': 'user',
        'content': [
            {"type": "text", "text": '''Please analyze the handwritten math content in this image.
                                        Accurately transcribe any mathematical expressions, equations, or LaTeX formulas or mathematical theoretical problem present.'''},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }]

    response = llm.chat.completions.create(
        model="llama-3.2-90b-vision-preview",
        messages=messages
    )
    return response.choices[0].message.content

def get_math_response(image_description):
    content = f"Image Description: {image_description}\n\n" if image_description else ""
    query = f"{content}User Question: Solve this math problem given in image description."
    
    messages = [
        {"role": "system", "content": "You are a helpful math assistant."},
        {"role": "user", "content": query}
    ]

    response = llm.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return remove_special_chars(response.choices[0].message.content)
