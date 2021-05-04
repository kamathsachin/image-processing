import PyPDF2

with open("./samplepdf/dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open("./samplepdf/tilt.pdf", "wb") as modified_file:
        writer.write(modified_file)