from PyPDF2 import PdfFileWriter, PdfFileReader
from os import listdir
import PySimpleGUI as sg

inputfile = sg.popup_get_file("Please choose file")


inputpdf = PdfFileReader(open(inputfile, "rb"))

outputdir = sg.popup_get_folder('Where to save') + '/'

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(f'{outputdir}document-page%s.pdf' % i, "wb") as outputStream:
        output.write(outputStream)
