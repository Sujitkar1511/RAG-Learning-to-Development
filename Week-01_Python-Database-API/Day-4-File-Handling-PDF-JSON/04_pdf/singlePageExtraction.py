import PyPDF2

#singe page text extraction

with open(r"D:\Users\HP\Downloads\Complete_Python_PDF_Handling_Guide.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]  # Extract text from the first page (index 0)
    text = page.extract_text()
    print(text)