import xlwt

from common.utils import readexcel


# 使用封装的函数readExcel，进行读取’111.xlsx‘，第一列
print(readexcel('../data/111.xlsx', 0))





#对excel 文件进行写的操作

# wr = xlwt.Workbook()
# ws = wr.add_sheet('test')   # 创建一个sheet名称
# ws.write(0,0,'测试')         # 在第一行第一列写values
# ws.write(0,1,'test')        # 在第一行第二列写values
# wr.save('222.xls')          # 保存文件名称