from reportlab.pdfgen import canvas

with open("text1.txt", 'r', encoding='utf-8') as text_file:
    text = text_file.read()

with open("output.pdf", 'wb') as pdf_file:
    c = canvas.Canvas(pdf_file)
    c.drawString(100, 750, text)   #x and y coordinates for the text position
    c.save()

    