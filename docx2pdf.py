from docx2pdf import convert
import os
import glob

current_dir = os.getcwd()
folder_name = "word_docs"
folder_directory = os.path.join(current_dir, folder_name)

docx_files = glob.glob(os.path.join(folder_directory, '*.docx'))

for docx_file in docx_files:
  if docx_file[-5:] == '.docx':
    convert(docx_file)

pdfs = glob.glob('*.pdf')