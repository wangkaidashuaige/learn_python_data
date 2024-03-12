


class people:
    fuse="yellow"
    language="中文"
    weight=125

    # 重构构造方法，初始化数据
    def __init__(self,name,age):
        print(f"创建了一个实例对象他的名字叫{name}，他今年{age}岁")
        self.name=name
        self.age=age


    def speakmimi(self):
        print("这是一个私有的方法")

    def speak(self):
        print("我说的是中国话")
        print("告诉你一个秘密，我的体重是：",self.weight)
        self.speakmimi()

wangkai=people("wangkai","24")
wangkai.speak()


print("私有属性及私有方法只能是在类的内部使用，实例对象或类对象是不可以子啊外部使用"
      "但是可以通过此种格式调用：对象._类型+私有属性/私有方法")
print("外部获取私有属性",wangkai._people_weight)
print("外部获取私有方法",wangkai._people_speakmimi())