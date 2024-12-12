import pytesseract
import cv2
import pyttsx3
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
def image_to_text(image_path):
    
    img = cv2.imread(image_path)
    
    text = pytesseract.image_to_string(img)
    return text
def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    
    
    rate = engine.getProperty('rate')  # Speed of speech
    engine.setProperty('rate', rate - 20)  # Slow down the speech
    
    
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    image_path = r'C:\Users\AL REHMAN LAPTOPS\Desktop\Waqas.png'  
    
    extracted_text = image_to_text(image_path)
    print("Extracted Text:\n", extracted_text)
    
    
    if extracted_text:
        text_to_speech(extracted_text)
    else:
        print("No text extracted from the image.")

