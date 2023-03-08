import cv2
import pytesseract

img = cv2.imread('./images/BALANCETE2022_page-0001.jpg')

print(pytesseract.get_languages(config=''))

result = pytesseract.image_to_string(img, lang='por')
print(result)