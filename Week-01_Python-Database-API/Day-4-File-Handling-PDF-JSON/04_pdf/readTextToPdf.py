import PyPDF2


#with function

# def read_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in reader.pages:
#             text += page.extract_text() 
#     return text

# text = read_text_from_pdf(r"D:\Users\HP\Downloads\Complete_Python_PDF_Handling_Guide.pdf")
# print(text)

#simple code without function

with open(r"D:\Users\HP\Downloads\Complete_Python_PDF_Handling_Guide.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

for t in text.splitlines():
    print(t)



