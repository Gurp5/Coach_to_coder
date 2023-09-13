from PyPDF2 import PdfReader

reader = PdfReader("Assertive_Testing_Reliable_Code.pdf")
number_of_pages = len(reader.pages)
all_texts  = []
all_pages = reader.pages
for page in all_pages:
    all_texts.append(page.extract_text())

all_text_combined = " ".join(all_texts)

individual_sentances = all_text_combined.split(".")
for sentance in individual_sentances:
    if("computer" in sentance):
        print(sentance)

# Some cool things to try out and put on GitHub:
# 1. resize 3 pictures using python - pillow
# 2. try to read in a word document and do some analysis on the text
# 3. try to create some audio files using python


