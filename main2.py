from docx2pdf import convert
import os
import glob

current_dir = os.getcwd()
word_docs_folder = "word_docs"
pdf_folder = "pdf_files"

word_docs_directory = os.path.join(current_dir, word_docs_folder)
pdf_directory = os.path.join(current_dir, pdf_folder)

docx_files = glob.glob(os.path.join(word_docs_directory, '*.docx'))

for docx_file in docx_files:
    if docx_file[-5:] == '.docx':
        # Specify the target folder for the PDF files
        convert(docx_file, os.path.join(pdf_directory, os.path.basename(docx_file[:-5] + '.pdf')))

# Now pdfs will contain the list of PDF files in the pdf_folder
pdfs = glob.glob(os.path.join(pdf_directory, '*.pdf'))
