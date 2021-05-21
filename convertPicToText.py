import requests
import urllib
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


url = 'http://www.epapersland.com/images/western-times.jpg'
urllib.request.urlretrieve(url, 'western-times.jpg')

img = Image.open('western-times.jpg')
document = pytesseract.image_to_string(img)
print(document)
