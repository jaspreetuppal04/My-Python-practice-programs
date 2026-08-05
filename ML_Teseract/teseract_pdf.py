import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path

# PDF path
pdf_path = "/Users/jaspreetuppal/Downloads/DAV_P1_69.pdf"

# Convert PDF into images (one image per page)
pdf_pages = convert_from_path(pdf_path)

print("Total Pages:", len(pdf_pages))

# Process each page
for page_num, page in enumerate(pdf_pages):

    print(f"\n----- PAGE {page_num + 1} -----")

    # Display the page
    plt.imshow(page)
    plt.axis("off")
    plt.show()

    # Extract text
    text = pytesseract.image_to_string(page)

    print("Extracted Text:\n")
    print(text)