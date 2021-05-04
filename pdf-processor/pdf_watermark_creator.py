import PyPDF2

source_file = PyPDF2.PdfFileReader(open("./samplepdf/twopage.pdf", "rb"))
watermark_file = PyPDF2.PdfFileReader(open("./samplepdf/wtr.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(source_file.getNumPages()):
    page = source_file.getPage(i)
    page.mergePage(watermark_file.getPage(0))
    output.addPage(page)

with open("./samplepdf/watermarked.pdf", "wb") as file:
    output.write(file)
