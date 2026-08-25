import PyPDF2

#page count
with open(r"D:\Users\HP\Downloads\Complete_Python_PDF_Handling_Guide.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page_count = len(reader.pages)
    print(f"Total number of pages: {page_count}")