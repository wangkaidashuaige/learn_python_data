import unittest, os
import pytest
from common.HTMLTestRunner import HTMLTestRunner

# unittest执行多条用例的方法
print (os.getcwd ())
path =os.getcwd ()
discover = unittest.defaultTestLoader.discover(path,pattern="search*.py",top_level_dir=None)
# runner=unittest.TextTestRunner()
# runner.run(discover)

# 生成html报告
filename ="D:\\test_UI_project\\HTML_report\\report.html"
fp = open (filename,"wb")
run = HTMLTestRunner(stream=fp, title=' selenium test',description="order testing")
run.run(discover)


## 生成allure报告
# if __name__ == '__main__':
#     unittest.main("--alluredir","temp")# 执行目录+文件，生成json文件格式内容
#     os.system("allure generate temp -o reports --clean")