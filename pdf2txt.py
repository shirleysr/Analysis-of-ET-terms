#实现了基本的pdf文件转txt,但在读取知网下载的pdf文献时存在问题
#下一步：实现文件的批量处理
#coding=utf-8
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.converter import PDFPageAggregator,TextConverter,XMLConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import  PDFTextExtractionNotAllowed,PDFPage
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import *
import os,re,io


##pdf格式转换
def pdf2txt(filePath,outPath):
    manager = PDFResourceManager()
    codec = 'utf-8'
    caching = True

    #创建一个pdf文档分析器，从文件中获取数据
    parser = PDFParser(filePath)
    #创建一个PDF文档对象存储文档结构，保存获取的数据
    document = PDFDocument(parser)
     # 检查文件是否允许文本提取
    if not document.is_extractable:
        #print("sorry,failed")
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共享资源
        rsrcmgr=PDFResourceManager()
        # 设定参数进行分析
        laparams=LAParams()
        # 创建一个PDF设备对象
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        # 创建一个PDF解释器对象，处理页面内容
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        # 处理文档中的每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage整个页面对象
            layout=device.get_result()

            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    with open('%s'%(outPath),'a') as f:
                        #“a”追加写，不会被覆盖；“w”重新写入，w有些文献会出错
                        #f.write(x.get_text()+ '\n')
                        f.write((x.get_text().encode("utf-8")+'\n'.encode("utf-8")).decode("utf-8","xmlcharrefreplace"))#decode("gbk","ignore"))
                        #type(x.get_text):class str;type(x.get_text).encode("utf-8"):class bytes;type(x.get_text).decode("utf-8"):class str;
                        # write对象为string,py3不支持二进制直接转化成字符串，因此编码语句要加上decode#

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
        pdf2txt(filePath,outPath)
        print("Saved "+outPath)
#pdfTotxt(u'C:\\Users\\Administrator\\Documents\\NoteExpress\\Libraries\\FullText\\教育技术学相关期刊文章')


filePath = open('testfiles\\1.pdf', 'rb')
outPath='testfiles\\1.txt'
pdf2txt(filePath,outPath)
#测试文件：python.pdf—成功；python_codeutf8.pdf—成功；22.pdf——成功#
# MOOC课程学习体验及本土化启示.pdf——失败；论开放大学办学体系体制机制建设的新路径.pdf——失败；法治与国家治理现代化_张文显.pdf——失败#