# This script runs on Windows only, and you must have Word installed.

import win32com.client # install with "pip install pywin32"
import docx
wordFilename = 'hello.docx'
pdfFilename = 'helloPDF.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.add_paragraph('This is the first paragraph.\nHello, World!')
doc.save(wordFilename)

wordFormatPDF = 17 # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wordFormatPDF)
docObj.Close()
wordObj.Quit()