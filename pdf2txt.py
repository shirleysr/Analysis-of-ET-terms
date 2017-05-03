#实现了基本的pdf文件转txt,但在读取知网下载的pdf文献时存在问题
#下一步：实现文件的批量处理

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import  PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import *

##格式转换
def Pdf2Txt(Path,Save_name):
    #创建一个pdf文档分析器
    parser = PDFParser(Path)
    #创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr=PDFResourceManager()
        # 设定参数进行分析
        laparams=LAParams()
        # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout=device.get_result()
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    with open('%s'%(Save_name),'a') as f:
                        #“a”追加写，不会被覆盖；“w”重新写入，w有些文献会出错
                        f.write((x.get_text().encode('utf-8')+'\n'.encode('utf-8')).decode("utf-8"))
                        #注意：write对象为string,py3不支持二进制直接转化成字符串，因此编码语句要加上decode##

Path = open('D:/pdfminer__text/testfiles/111.pdf', 'rb')
Pdf2Txt(Path,'111.txt')
#测试文件：python.pdf—成功；python_codeutf8.pdf—成功；22.pdf——成功#
# MOOC课程学习体验及本土化启示.pdf——失败；论开放大学办学体系体制机制建设的新路径.pdf——失败；法治与国家治理现代化_张文显.pdf——失败#