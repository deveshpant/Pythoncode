from pdf2docx import Converter
pdf_file = 'Fidelityletter.pdf'
docx_file = 'Fidelityletter.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()