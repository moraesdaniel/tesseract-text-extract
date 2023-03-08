import cv2
import pytesseract


print(pytesseract.get_languages(config=''))

img = cv2.imread('./images/BALANCETE2022_page-0001.jpg')
result = pytesseract.image_to_string(img, lang='por')
print(result)