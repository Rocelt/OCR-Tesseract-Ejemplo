import cv2
import pytesseract
import numpy as np
import time

# Para Windows (ajusta la ruta según tu instalación)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def procesar_imagen(imagen):
    
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbral adaptativo
    _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Aplicar dilatación para conectar los componentes de texto
    kernel = np.ones((1, 1), np.uint8)
    umbral = cv2.dilate(umbral, kernel, iterations=1)
    
    return umbral

def main():
    # Inicializar la cámara
    cap = cv2.VideoCapture(1)
    
    # Verificar si la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return
    
    # Configurar el tamaño de la ventana
    cv2.namedWindow("Extracción de texto en tiempo real", cv2.WINDOW_NORMAL)
    
    ultimo_tiempo_ocr = time.time()
    texto_actual = ""
    
    while True:
        # Capturar frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: No se pudo leer el frame.")
            break
        
        # Crear una copia del frame para mostrar
        frame_mostrar = frame.copy()
        
        # Procesar OCR cada 1 segundo para no sobrecargar el sistema
        tiempo_actual = time.time()
        if tiempo_actual - ultimo_tiempo_ocr > 1:
            # Procesar la imagen para mejorar OCR
            imagen_procesada = procesar_imagen(frame)
            
            # Extraer texto con Tesseract
            try:
                texto_actual = pytesseract.image_to_string(imagen_procesada)
                ultimo_tiempo_ocr = tiempo_actual
            except Exception as e:
                print(f"Error en OCR: {e}")
        
        # Mostrar el texto extraído en la imagen
        if texto_actual:
            # Dividir el texto en líneas
            lineas = texto_actual.split('\n')
            y = 30
            for i, linea in enumerate(lineas):
                if linea.strip():  # Ignorar líneas vacías
                    cv2.putText(frame_mostrar, linea, (10, y), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    y += 30
        
        # Mostrar el frame con el texto extraído
        cv2.putText(frame_mostrar, "Presiona 'q' para salir", (10, frame_mostrar.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Extracción de texto en tiempo real", frame_mostrar)
        
        # Esperar por la tecla 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()