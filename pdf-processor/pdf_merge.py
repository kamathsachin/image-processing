import PyPDF2
import sys

# Read file names from the command line
inputs = sys.argv[1:]  # Reads all the argument with and after index 1

# Create a function to loop through the list and merge
def merge_pdf(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write("./samplepdf/super.pdf")


# Call the function
merge_pdf(inputs)