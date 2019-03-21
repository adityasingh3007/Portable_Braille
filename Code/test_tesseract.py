try:

    from PIL import Image

except ImportError:

    import Image

import pytesseract

import cv2

import numpy as np

 

text = cv2.imread('text.jpg')

cv2.imshow('text',text)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(pytesseract.image_to_string(text))