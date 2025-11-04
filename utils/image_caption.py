from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

print("Loading AI model... (this might take a minute the first time)")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("✅ Model loaded successfully!")

def generate_caption(image_path):
    """
    Generate a caption for an image using the BLIP model.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        str: Generated caption describing the image
    """
    try:
        image = Image.open(image_path).convert('RGB')
      
        inputs = processor(image, return_tensors="pt")
    
        with torch.no_grad():
            output = model.generate(**inputs, max_length=50)
      
        caption = processor.decode(output[0], skip_special_tokens=True)
        
        caption = enhance_caption(caption)
        
        return caption
    
    except Exception as e:
        print(f"Error generating caption: {str(e)}")
        return "Unable to generate description for this image."

def enhance_caption(caption):
    """
    Make the caption more descriptive and natural.
    This is a simple enhancement - you can make it more sophisticated!
    """
    caption = caption.strip()
    if caption:
        caption = caption[0].upper() + caption[1:]
    
    if not caption.endswith('.'):
        caption += '.'
  
    descriptive_caption = f"This image shows {caption}"
    
    return descriptive_caption
