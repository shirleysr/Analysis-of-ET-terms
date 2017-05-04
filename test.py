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
        with open('%s' % (outPath), 'a') as f:
            f.write(convertedPDF)
    infile.close();converter.close();output.close()
    return 0

#一个文件夹下的所有pdf文档转换成txt
def pdfTotxt(fileDir):
    files=os.listdir(fileDir)
    tarDir=fileDir+'txt'
    if not os.path.exists(tarDir):
        os.mkdir(tarDir)
    replace=re.compile(r'\.pdf',re.I)
    for file in files:
        filePath=fileDir+'\\'+file
        outPath=tarDir+'\\'+re.sub(replace,'',file)+'.txt'
        convert(filePath,outPath)
        print("Saved "+outPath)

pdfTotxt(u'F:\\期刊文献分析\\test_filedir')



