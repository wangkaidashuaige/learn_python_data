import os
import yaml

class YamlUtil:
    # 读取extract.yml文件
    def read_extract_yml(self):
        with open(os.getcwd()+"/exctract.yml",mode='r',encoding='utf-8') as f:
             # 打开exctract.yml               读取      编码格式
            values = yaml.load(stream=f,loader=yaml.Fulloader)
                        # 加载文件流     加载方式
            return values;


    # 写入extract.yml文件
    def  wirte_extract_yml(self,data):
        with open(os.getcwd()+"/exctract.yml",mode='a',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    # 清除extract.yml文件
    def clear_extract_yml(self):
        with open(os.getcwd() + "/exctract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例的yml文件
    def read_testcase_yml(self,yaml_name):
        with open(os.getcwd()+"/testcase.yml/"+yaml_name,mode='r',encoding='utf-8') as f:
               # 打开exctract.yml               读取      编码格式
            values = yaml.load(stream=f,loader=yaml.Fulloader)
                        # 加载文件流         加载方式
            return values;