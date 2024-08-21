

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

def generate_image_description(image_url):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    image = Image.open(requests.get(image_url, stream=True).raw)
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    description = processor.decode(output[0], skip_special_tokens=True)
    return description
