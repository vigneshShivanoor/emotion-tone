from transformers import BlipProcessor, BlipForConditionalGeneration
import requests
from PIL import Image
import torch

def generate_caption(image_url):
    # Load pre-trained model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Download the image
    image = Image.open(requests.get(image_url, stream=True).raw)

    # Preprocess and generate caption
    inputs = processor(image, return_tensors="pt").to(torch.device("cpu"))
    caption = model.generate(**inputs)
    
    return processor.decode(caption[0], skip_special_tokens=True)
