import pytesseract
from PIL import Image
import fitz  # PyMuPDF

def extract_text_from_scanned_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    
    # Initialize text variable
    text = ""
    
    # Iterate through the pages and perform OCR
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text += pytesseract.image_to_string(img)
    
    return text

# Example usage
pdf_path = '/home/yuv/Documents/docsss/DBMS/mca-1-sem-relational-database-management-system-mcan-102-2023.pdf'
extracted_text = extract_text_from_scanned_pdf(pdf_path)
print(extracted_text)
