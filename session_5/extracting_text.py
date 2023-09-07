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
    if("module" in sentance):
        print(sentance)


