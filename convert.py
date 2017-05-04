from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,os,re

def convert(filePath,outPath):
    manager = PDFResourceManager()
    codec = 'utf-8'

    output = io.StringIO()
    converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(filePath, 'rb')
    for page in PDFPage.get_pages(infile, check_extractable=True):
        interpreter.process_page(page)
    convertedPDF = output.getvalue()
    infile.close();
    converter.close();
    output.close()
    return convertedPDF

filePDF  = 'F:\\期刊文献分析\\test_filedir\\“互联网+”时代知识观的转变_从共建共享到众传共推.pdf'
fileTXT  = 'testfiles\\123.txt'

convertedPDF = convert(filePDF,fileTXT )
fileConverted = open(fileTXT, "w")
fileConverted.write(convertedPDF)
fileConverted.close()
print(convertedPDF)