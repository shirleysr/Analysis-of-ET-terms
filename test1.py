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
#pdfTotxt(u'C:\\Users\\Administrator\\Documents\\NoteExpress\\Libraries\\FullText\\教育技术学相关期刊文章')