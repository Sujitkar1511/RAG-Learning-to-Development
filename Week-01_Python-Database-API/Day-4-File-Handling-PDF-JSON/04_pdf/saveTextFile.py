import PyPDF2

with open(r"D:\Users\HP\Downloads\Complete_Python_PDF_Handling_Guide.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    with open("text.txt", 'w', encoding='utf-8') as text_file:
        for page in reader.pages:
            text = page.extract_text()
            text_file.write(text + "\n")

print("Text extracted and saved to text.txt")
