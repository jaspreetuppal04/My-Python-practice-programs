import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

image_path = "/Users/jaspreetuppal/Downloads/_Years Of Sustainability.PNG"

img = Image.open(image_path)

plt.imshow(img)
plt.axis("off")
plt.show()

text = pytesseract.image_to_string(img)

print("\nExtracted Text:\n")
print(text)

text = pytesseract.image_to_string(img)
print(text)