# @pytest.fixtrue()一般会和conftest.py文件-起使用
# conftest.py名称是固定的,功能很强大。
# 1.conftest.py文件是单独存放@pytest.fixtrue()的方法,用处是可以在多个py文件之间共享前置配置。
# 2.conftest.py里面的方法在调用时不需要导入,可以直接使用。
# 3..conftest.py可以有多个。也可以有多个不同层级。

# 部分前置:
# @pytest.fixtrue(scope="作用域", params="数据驱动", autouse="自动执行",ids="自定义参数名"name="重命名")、
# 作用域: function, class, module, package/session可以通过yield唤醒类似teardown的功能,简单理解就是返回。
# yield和return都表示返回数据的意思,只是区分在于,yield返回多次以及多个数据,return只会返回一次,return之后不能接代码。
import pytest

from common.yaml_util import YamlUtil

@pytest.fixture(scope="function")
def conncet_database():
    print("数据库连接")
    yield
    print("关闭数据库")

@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yml()