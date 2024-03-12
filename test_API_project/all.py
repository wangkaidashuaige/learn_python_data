import os # os.system模块提供对操作系统功能的访问
import pytest

if __name__ == '__main__':
    # pytest.main(["Studying/mozi_tag.py","-sv","--alluredir","temp"])# 执行目录+文件，生成json文件格式内容
    # os.system("allure generate temp -o reports --clean")            # 使用allure报告吧JSON内容产生报告到reports中
    # # os.system("start allure serve temp -o reports --clean")


    pytest.main(["-sv","--alluredir","temp"])# 执行目录+文件，生成json文件格式内容
    os.system("allure generate temp -o reports --clean")            # 使用allure报告吧JSON内容产生报告到reports中
