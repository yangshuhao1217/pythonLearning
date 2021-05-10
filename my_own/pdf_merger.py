from PyPDF2 import PdfFileMerger
from os import listdir

input_dir = "C:/Users/yangshuhao/Documents/Work/pdf_work/"


merge_list = []

for i in listdir(input_dir):
    if not i.endswith('.pdf'):
        continue
    merge_list.append(input_dir + i)

merger = PdfFileMerger()

for pdf in merge_list:
    merger.append(pdf)

merger.write("C:/Users/yangshuhao/Documents/Work/pdf_work/merged_file.pdf")
merger.close()
