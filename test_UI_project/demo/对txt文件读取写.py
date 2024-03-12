import os



print (os. getcwd ())
'''# 获取txt文件路径,相对路径'''
print(os. getcwd().split('demo')[0]+'111.txt')
print(os. getcwd()[:-10])
print(os. getewd()[0:3])
'''# 读文件'''
f = open('../data/111.txt', 'r')
print(f.read())# 全部文件
print(f.read(1))# -个字符
print(f.readline())# 按行进行读取
print(f.readlines()) # 放列表
f. close () # 关闭
'''写文件'''
f = open ('../data/222.txt', 'w')     # 直接写文件
f.write ("python selenium")  # 写文件里面的内容

f = open ('333.txt','w') # 复杂点的写文件
s=['aa\n','bb\n','cc\n']# 文件里面的内容
f.writelines(s)
f.close ()#作业,对文件操作改成函数