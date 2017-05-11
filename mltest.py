# 安装pdfminer包：进入pdfminer3k-1.3.1文件下的命令窗口，输入python setup.py install
#  导入包
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,os,re

# 将pdf文件转化为txt文件。输入:pdf文件夹，得到txt文件output.txt
def Pdf_to_txt(fileDir):
    codec = 'utf-8'
    outfile="output.txt"
    files = os.listdir(fileDir)
    print (files)
    for file in files:
        manager = PDFResourceManager()
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        filePath = fileDir + '\\' + file
        infile = open(filePath, 'rb')
        for page in PDFPage.get_pages(infile, check_extractable=True):
           interpreter.process_page(page)
           convertedPDF = output.getvalue()
        print(convertedPDF)
        with open('%s' % (outfile), 'a+b') as f:
            f.write((os.path.basename(file)+convertedPDF).encode())
            #python3编码转换新方法“wb”,encode():http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
        infile.readline().split()
        infile.close()
        output.close()
        converter.close()
    print("Saved")
    return 0

Pdf_to_txt(u'testfiles')
file=open("outfile.txt")
file.readline().split()