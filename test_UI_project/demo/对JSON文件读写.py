import json

js ={"android":"appium","web":"selenium","interface":"requests"}
print (type (js)) # 打印出字典dict类型
print (type (json.dumps (js)))      # dumps、dict转换str字符串类型
print (type (json.loads (json.dumps (js))))     #loads、str字符串类型转换dict字典类型

# 对json文件读操作
# f = open("11.json",'r')   # 打开文件11。JSON文件、、r = read  读模式
# print(json.load(f))

# #对json文件写操作
f = open ("../data/11.json", "w") # 创建文件11.JSON文件、、w = write  写模式
# json.dump(js,f)           # 执行 f 变量里的内容