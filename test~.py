# 安装pdfminer包：https://pypi.python.org/pypi/pdfminer3k 进入pdfminer3k-1.3.1文件下的命令窗口，输入python setup.py install
# 安装pdfminer.six
# 导入包

##为pdf加入文件名和时间
# 思路：
# 遍历文章题录filelist1，将所有题目和出版时间放在一个二维数组中；
# 遍历列表题目，写入题目、出版时间，
# 并从另一个文件夹中找出该pdf文件，输出文件txt
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,os,re

# 将pdf文件转化为txt文件。输入:pdf文件夹，得到txt文件output.txt
def Pdf_to_txt(fileDir,outfile):
    codec = 'utf-8'
    files = os.listdir(fileDir)

    for file in files:
        manager = PDFResourceManager()
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        filePath = fileDir + '\\' + file
        f = open(outfile,'a+b')
        with open(filePath, 'rb') as infile:
            content =[]# 定义一个数组变量用于暂存数据
            content.append('##'+os.path.basename(filePath).split('.')[0]+'##')
            # with open('%s' % (outfile), 'a+b') as f:
            #     f.write(('##'+os.path.basename(filePath).split('.')[0]+'##').encode())
            for page in PDFPage.get_pages(infile, check_extractable=True):
               interpreter.process_page(page)
               convertedPDF = output.getvalue()
            print(convertedPDF)
        # python3编码转换新方法“wb”,encode():http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
            content.append(convertedPDF)
        with open('%s' % (outfile), 'a+b') as f:
           f.write(''.join(content).encode())
        output.close()
        converter.close()
        f.close()
    print("-----------------------------------完成pdf转化至txt--------------------------------------")
    return 0

# 清理txt文本语料。输入：txt文本，得到只有中字符和句中标点符号的txt文档
def clean_txt(outfile):
    with open(outfile, 'rb')as f:
        content = f.read().decode('utf-8')
    # p定义了要挑选出的内容，其中\u4e00-\u9fff为中文字符的Unicode编码区间，\u3002\uFF0C分别表示句号与逗号
    ##<?<=/d>a
    p = re.compile(u"[\u4e00-\u9fff+\u3002\uFF0C]")
    # x将找出的符合条件的内容列表连接在一起输出
    x = ''.join(re.findall(p, content))
    # 删除x中连续出现的重复内容，这里对逗号进行了处理
    final_result = re.sub(u"[\uFF0C]{2,}", "", x)
    with open(cleaned_file, "w")as outfile:
        outfile.write(final_result)
    print(final_result)
    print("-----------------------------------------完成txt清洗-------------------------------------")
    return 0

fileDir=u'test\\files1'
outfile = "test\output.txt"
cleaned_file = "test\\txt_cleaned.txt"
Pdf_to_txt(fileDir,outfile)
clean_txt(outfile)