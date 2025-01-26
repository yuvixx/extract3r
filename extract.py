import os
import re
from PIL import Image
import pytesseract

def clean_text(text):
    """
    Clean and structure the extracted text.
    :param text: Raw text extracted from the image.
    :return: Cleaned and structured text.
    """
    # Remove unwanted newlines and extra spaces
    text = re.sub(r'\s+', ' ', text.strip())

    # Optionally, remove non-alphanumeric characters (except spaces)
    text = re.sub(r'[^A-Za-z0-9\s.,!?\'"-]', '', text)

    # You can add more text cleaning or structuring steps here as needed
    return text

def extract_text(image_path):
    """
    Extract text from an image and structure it.
    :param image_path: Path to the image file.
    :return: Dictionary with structured text or an error message.
    """
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            return {'error': 'Image file not found'}
        
        # Open the image
        img = Image.open(image_path)
        
        # Extract text using pytesseract
        raw_text = pytesseract.image_to_string(img)

        if not raw_text.strip():
            return {'error': 'No text detected in the image'}

        # Clean and structure the text
        structured_text = clean_text(raw_text)

        return {'text': structured_text}
    
    except Exception as e:
        return {'error': str(e)}

# Example usage
image_path = 'file_path'
result = extract_text(image_path)

# Print the result
print(result)
