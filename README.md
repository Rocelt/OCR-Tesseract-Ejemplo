# OCR-Tesseract-Ejemplo

# Extractor de Texto con Tesseract OCR

Esta herramienta permite extraer texto de imágenes utilizando la tecnología de reconocimiento óptico de caracteres (OCR) de Tesseract. El script está desarrollado en Python y proporciona una interfaz simple para procesar imágenes y obtener el texto contenido en ellas.

## Características

- Extracción de texto de imágenes en diferentes formatos (JPG, PNG, BMP, etc.)
- Soporte para múltiples idiomas

## Requisitos previos

### 1. Instalar Tesseract OCR

#### Windows
- Descarga e instala Tesseract desde [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- Asegúrate de marcar los idiomas adicionales que necesites durante la instalación
- Añade la ruta de instalación de Tesseract a las variables de entorno PATH

### 2. Instalar dependencias de Python
```bash
pip install pytesseract pillow
```

## Instalación

1. Clona este repositorio o descarga el archivo `ocr.py`
2. Instala las dependencias mencionadas anteriormente

## Uso

### Uso básico
```bash
python image_to_text.py ruta/a/tu/imagen.jpg
```

### Códigos de idioma comunes
- `spa`: Español
- `eng`: Inglés
- `fra`: Francés
- `deu`: Alemán
- `ita`: Italiano
- `por`: Portugués

## Ejemplos

### Extraer texto
```bash
python image_to_text.py factura.jpg
```

## Resolución de problemas

### Error "tesseract is not installed or it's not in your PATH"
- Asegúrate de que Tesseract esté correctamente instalado
- Verifica que la ruta de instalación esté en la variable PATH
- En Windows, puedes especificar manualmente la ruta de Tesseract en el código:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

### Texto extraído con baja precisión
- Asegúrate de que la imagen sea clara y tenga buen contraste
- Prueba a preprocesar la imagen con técnicas de mejora de contraste o eliminación de ruido
- Verifica que estás usando el idioma correcto para la detección
