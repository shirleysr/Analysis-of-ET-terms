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

def pdf_to_txt(filelist):
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
        #根据key值找文件
        filePath='test\\files1\\'+i+'.pdf'
        if not os.path.exists(filePath):
            continue
        else:
          manager = PDFResourceManager()
          output = io.StringIO()
          converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
          interpreter = PDFPageInterpreter(manager, converter)
          f = open(outfile, 'a+b')
          with open(filePath, 'rb') as infile:
               content = []  # 定义一个数组变量用于暂存数据i
               content.append('###'+i+'$'+Dict[i] +'$'+'###')#将标题用##符号包围起来
               for page in PDFPage.get_pages(infile, check_extractable=True):
                   interpreter.process_page(page)
                   convertedPDF = output.getvalue()
               print(convertedPDF)
            # python3编码转换新方法“wb”,encode():http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
               content.append(convertedPDF)
          with open('%s' % (outfile), 'wb') as f:
             f.write(''.join(content).encode())
             print("-----------------------------------完成该篇文章的pdf转化--------------------------------------")
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

    p = re.compile(r'(?<=##)\S.+(?=##)|[\u4e00-\u9fff+\u3002\uFF0C]')
    # x将找出的符合条件的内容列表连接在一起输出
    x = ''.join(re.findall(p, content))
    # 删除x中连续出现的重复内容，这里对逗号进行了处理
    final_result = re.sub(u"[\uFF0C|\u3002|\u002B]{2,}", "", x)
    with open(cleaned_file, "w")as outfile:
        outfile.write(final_result)
    print(final_result)
    print("-----------------------------------------完成txt清洗-------------------------------------")
    return 0


fileDir = u'test\\files1'
filelist=u'test\\filelist1.txt'
outfile = "test\output.txt"
cleaned_file = "test\\txt_cleaned.txt"
pdf_to_txt(filelist)
clean_txt(outfile)