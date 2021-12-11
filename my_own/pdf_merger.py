from PyPDF2 import PdfFileMerger
from os import listdir
import PySimpleGUI as sg

input_dir = sg.popup_get_folder('Please choose folder')


merge_list = []

for i in listdir(input_dir):
    if not i.endswith('.pdf'):
        continue
    merge_list.append(i)

merger = PdfFileMerger(strict=False)

for pdf in merge_list:
    merger.append(pdf)

output_dir = sg.popup_get_folder('Where to save') + '/'
output_name = f'{output_dir}merged_file.pdf'

merger.write(output_name)
merger.close()
