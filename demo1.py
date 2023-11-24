#将数据输出在文件中 ,注意.1. 所指定的盘符在存在，2. 使用file=fp
fp = open('D:/text.txt','a+')#a+如果文件不存在就创建，存在就在文件内容的后面继续追加
print('helloworld',file=fp)
fp.close()

#不进行换行输出（输出内容在一行中）
print('hello','world','python')