import pytesseract
import matplotlib.pyplot as plt
# For better accuracy
import cv2
import numpy as np
from PIL import Image

img_cv = cv2.imread("/Users/jaspreetuppal/Downloads/_Years Of Sustainability.PNG")

# Convert to grayscale
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# OCR
text = pytesseract.image_to_string(thresh)
print(text)