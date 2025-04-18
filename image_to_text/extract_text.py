from PIL import Image
import pytesseract
import os

# OPTIONAL: If tesseract is not in your PATH, set it manually:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        return f"❌ File not found: {image_path}"
    
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"❌ Error processing image: {e}"

if __name__ == "__main__":
    print("🖼️ Image to Text (OCR)\n")
    path = input("Enter image path: ").strip()
    result = extract_text_from_image(path)
    
    print("\n📝 Extracted Text:\n")
    print(result if result else "⚠️ No text detected.")

