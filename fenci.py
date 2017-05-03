#encoding=utf-8
import jieba

seg_list = jieba.cut("我是一个粉刷匠粉刷本领强我是一条小青龙educational technology大数据社会主义建构主义学说", cut_all=True)
print ("Full Mode:", "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut("我是一个粉刷匠粉刷本领强我有许多小秘密educational technology大数据社会主义建构主义学说", cut_all=False)
print ("Default Mode:", "/ ".join(seg_list) ) # 精确模式
seg_list = jieba.cut("我是一个粉刷匠粉刷本领强谁也不知道educational technology大数据社会主义建构主义学说")  # 默认是精确模式
print (", ".join(seg_list))
seg_list = jieba.cut_for_search("我是一个粉刷匠粉刷本领强我有多少秘密哈哈educational technology大数据社会主义建构主义学说")  # 搜索引擎模式
print (", ".join(seg_list))