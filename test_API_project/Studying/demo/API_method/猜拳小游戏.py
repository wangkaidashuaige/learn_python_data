# 分割获取张三
data = "name=zhangsan&dahsodjoa"
result = data.split('=')
result1 = result[1].split("&")[0]
print(result1)


def calculate_score(lists):
    guan_win= 0
    zhang_win = 0
    ping_round = 0

    for list in lists:
        guan = list[0]
        zhang = list[-1]
        if (guan == '石头'and zhang=='剪刀') or (guan == '剪刀' and zhang=='布') or (guan == '布' and zhang=='剪刀'):
            guan_win +=1
            print("关羽赢一分")
        elif guan==zhang:
            ping_round +=1
            print("平手")
        else:
            zhang_win +=1
            print("张飞赢一分")
    while guan_win > zhang_win:
        print('关羽不愧为武圣！！！')
        return
    if guan_win == zhang_win:
        print('旗鼓相当')
        return
    else:
        print('张翼德在此')
        return

list=[['石头','剪刀'],['剪刀','剪刀'],['布','石头'],['石头','剪刀']]
calculate_score(list)
