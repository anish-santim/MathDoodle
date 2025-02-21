# MathDoodle - AI Handwritten Math Solver

MathDoodle is a web-based AI-powered application that converts handwritten mathematical expressions into accurate solutions. It uses **Gradio** for the UI, **OpenCV** for image preprocessing, and **Groq's AI models(llama-3.2-90b-vision-preview)** for OCR and **Groq's AI models(llama-3.3-70b-versatile)** for generating math solutions.

## Features
- Sketchpad for handwriting math equations
- AI-powered OCR and equation solving
- Image preprocessing for improved recognition
- Interactive and easy-to-use UI with **Gradio**

## Why used Groq's AI models?
- **llama-3.2-90b-vision-preview**: The Llama-3.2-90B-Vision model can process both text and images, allowing it to perform tasks that require understanding and reasoning about visual content alongside textual information. This makes it suitable for applications like image captioning, visual question answering, and more complex image-based interactions.
- **llama-3.3-70b-versatile**: The Llama-3.3-70B-Versatile model is designed to handle a wide range of tasks, including text generation, question answering, and more. It's a versatile model that can be fine-tuned for specific tasks or used as a general-purpose language model.


## Project Structure
```
math_doodle_project/
│── app.py              # Main application file (Gradio UI)
│── utils.py            # Helper functions (image encoding, cleaning text, etc.)
│── ai_handler.py       # AI interactions (OCR and math solution generation)
│── image_processor.py  # Image processing and handling
│── requirements.txt    # List of dependencies
│── .env                # Environment variables (API keys)
│── README.md           # Project instructions
```

## Installation
Make sure you have **Python 3.8+** installed, then follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/math_doodle_project.git
cd math_doodle_project
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add your **Groq API key**:
```
GROQ_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
gradio app.py
```
This will start a local Gradio UI where you can use the sketchpad to draw math equations and get AI-generated solutions.

