import pytesseract
from PIL import Image
import argparse

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def extract_text_from_image(image_path, lang='spa'):

    try:
        # Abrir la imagen con PIL
        img = Image.open(image_path)
        
        # Usar pytesseract para convertir la imagen a texto
        texto = pytesseract.image_to_string(img, lang=lang)
        
        return texto
    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"

def main():
    image = input("Ingresa el path de la imagen a utilizar : ")

    
    # Extraer texto
    texto = extract_text_from_image(image, 'spa')
    
    # Mostrar el resultado
    print("\nTexto extraído:")
    print("==============")
    print(texto)

if __name__ == "__main__":
    main()