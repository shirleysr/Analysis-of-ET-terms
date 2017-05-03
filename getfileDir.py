import os
##读取全部文件名
def getfileDir(path):
   file_list=[]
   for p,d,f in os.walk(path):
       for f1 in f:
          file_list.append(os.path.join(p,f1))
   #return file_list
   print(file_list)


path='C:\\Users\Administrator\Documents\NoteExpress\Libraries\FullText\教育技术学相关期刊文章'
getfileDir(path)




