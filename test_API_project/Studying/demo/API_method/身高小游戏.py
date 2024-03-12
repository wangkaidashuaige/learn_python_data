shengao = input("请输入你的身高（单位厘米）：")
tizhong = input("请输入你的体重（单位公斤）：")
age = input("请输入你的年龄：")

while age < "10":
    print("年龄太小了不行，上小孩那桌吃饭去")
    break

while int(age) >= 10 and int(age) < 60:
    if (int(tizhong) / int(shengao)) ** 2 > 24:
        print(f"你的身高是{shengao}厘米，你的体重是{tizhong}公斤，你的年龄是{age}岁")
        print("吃化肥了么")
        break
    elif (int(tizhong) / int(shengao)) ** 2 < 18:
        print(f"你的身高是{shengao}厘米，你的体重是{tizhong}公斤，你的年龄是{age}岁")
        print("细狗")
        break
    else:
        print(f"你的身高是{shengao}厘米，你的体重是{tizhong}公斤，你的年龄是{age}岁")
        print("挺正常啊")
        break

else:
    print("年龄太大了，不行奥，玩不了")
quit()
