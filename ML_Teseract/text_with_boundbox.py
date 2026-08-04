import pytesseract

data = pytesseract.image_to_data("/Users/jaspreetuppal/Downloads/_Years Of Sustainability.PNG", output_type=pytesseract.Output.DICT)

for i in range(len(data["text"])):
    if int(data["conf"][i]) > 50:
        print(data["text"][i], data["conf"][i])