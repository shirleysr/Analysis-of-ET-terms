##为pdf加入文件名和时间
# 思路：
# 遍历文章题录filelist1，将所有题目和出版时间放在一个字典中；
# 遍历字典中的key：标题，在最终文件中写入标题、出版时间，
# 并从另一个文件夹中找出该pdf文件，输出文件txt
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,os,re

def add_sth(filelist):
    codec = 'utf-8'
    mylist=dict.fromkeys(['title', 'year'], ('unknow'))
    with open (filelist,'r') as f:
        i=f.read()
        files = os.listdir(fileDir)
        p1 = re.compile(r'(?<=%T ).+(?=' ')')#%T开头的字符串表示标题
        p2 = re.compile(r'(?<=%D ).+(?=' ')')#%D开头的字符串表示时间
        title=re.findall(p1,i)
        year=re.findall(p2,i)
        Dict=dict(zip(title,year))
        print(Dict)
    for i in Dict.keys():
        print(i)
        #根据key值找文件
        filePath='test\\files1\\'+i+'.pdf'
        manager = PDFResourceManager()
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        f = open(outfile, 'a+b')
        with open(filePath, 'rb') as infile:
            content = []  # 定义一个数组变量用于暂存数据i
            content.append('##' +i+'$'+Dict.get(i) +'$'+ '##')#将标题用##符号包围起来
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


fileDir = u'test\\files1'
filelist=u'test\\filelist1.txt'
outfile = "test\output.txt"
add_sth(filelist)






    # for file in files:
    #     manager = PDFResourceManager()
    #     output = io.StringIO()
    #     converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
    #     interpreter = PDFPageInterpreter(manager, converter)
    #     filePath = fileDir + '\\' + file
    #     f = open(outfile,'a+b')
    #     with open(filePath, 'rb') as infile:
    #         content =[]# 定义一个数组变量用于暂存数据
    #         content.append('##'+os.path.basename(filePath).split('.')[0]+'##')
    #         # with open('%s' % (outfile), 'a+b') as f:
    #         #     f.write(('##'+os.path.basename(filePath).split('.')[0]+'##').encode())
    #         for page in PDFPage.get_pages(infile, check_extractable=True):
    #            interpreter.process_page(page)
    #            convertedPDF = output.getvalue()
    #         print(convertedPDF)
    #     # python3编码转换新方法“wb”,encode():http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
    #         content.append(convertedPDF)
    #     with open('%s' % (outfile), 'a+b') as f:
    #        f.write(''.join(content).encode())
    #     output.close()
    #     converter.close()
    #     f.close()
    # print("-----------------------------------完成pdf转化至txt--------------------------------------")
    # return 0