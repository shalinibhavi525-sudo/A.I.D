import requests
from PIL import Image
import base64
from io import BytesIO

def generate_caption(image_path):
    """
    Generate caption using Hugging Face API (no model download needed!)
    """
    try:
        # Read image and convert to base64
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            buffered = BytesIO()
            img.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Call Hugging Face API (free!)
        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
        
        with open(image_path, "rb") as f:
            data = f.read()
        
        response = requests.post(API_URL, data=data)
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0:
            caption = result[0].get('generated_text', 'Unable to generate description.')
        else:
            caption = "Unable to generate description."
        
        return enhance_caption(caption)
    
    except Exception as e:
        print(f"Error generating caption: {str(e)}")
        return "Unable to generate description for this image."

def enhance_caption(caption):
    caption = caption.strip()
    if caption:
        caption = caption[0].upper() + caption[1:]
    
    if not caption.endswith('.'):
        caption += '.'
    
    if not caption.lower().startswith('this'):
        caption = f"This image shows {caption}"
    
    return caption
