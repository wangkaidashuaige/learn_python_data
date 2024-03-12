# !/user/bin/env python3
# -*- coding: utf-8 -*-
import random
while True:
    print("\t\t\t英雄联盟商城界面\n")
    print("~*"*25)
    print("\t\t\t1.用户登录\n")
    print("\t\t\t2.用户注册\n")
    print("\t\t\t3.退出系统\n")
    print("~*"*25)

    a = int(input('请输入你的选项1-3:'))
    if a == 1:
        username =input('请输入你的用户名：')
        password = input('请输入你的密码：')
        if username=='幼杀快发歌吧' and password == '8888':
            print('恭喜您，登陆成功')
            while True:
                print("\t\t\t英雄联盟商城界面\n")
                print("~*" * 25)
                print("\t\t\t1.进入英雄商店\n")
                print("\t\t\t2.休闲小游戏\n")
                print("\t\t\t3.退出登陆\n")
                print("~*" * 25)
                choice = input('请输入您的选择：')
                if choice == '1':
                    print('新款皮肤2.8折，您需要支付50')
                    num = int(input('请你输入您要购买的数量：'))
                    sum1 = num * 50
                    print('您购买的皮肤，需要支付的金额是：', sum1)
                    pay = int(input('请支付商品需要的金额：'))
                    # 循环 支付错误需要重新支付
                    if pay == sum1:
                        print('恭喜，购买成功')
                    else:
                        print('抱歉，支付金额有问题，请重新支付')
                elif choice == '2':
                    print('成功进入休闲小游戏')
                    words = ('python', 'jumble', 'easy', 'difficult', 'answer', 'continue', 'phone', 'position', 'game')
                    right = 'Y'
                    print("欢迎参加猜单词游戏！")
                    while right == 'Y' or right == 'y':
                        word = random.choice(words)#选择一个单词
                        correct = word
                        new_word = ''
                        while word: #把每个下标的字母循环取出来
                            pos = random.randrange(len(word))
                            new_word += word[pos]
                            # 将word单词下标为pos的字母去掉，取pos前面和后面的字母组成新的word
                            word = word[:pos] + word[(pos + 1):]  # 除去选出来的字母
                        print("你要猜测的单词为：", new_word)
                        guess = input("请输入你的答案：")
                        count = 1
                        while count < 5:
                            if guess != correct:
                                guess = input("输入的单词错误，请重新输入：")
                                count += 1
                            else:
                                print("输入的单词正确，正确单词为：", correct)
                                break
                        if count == 5:
                            print("您已猜错5次，正确的单词为：", correct)
                        right = input("是否继续，Y/N：")

                else:
                    break

        else:
            print('用户名或密码错误，请重新登陆，按任意键继续：')
    elif a == 2:
        phone = input('请输入你要注册的手机号：')
        b = len(phone) #手机号长度
        if b == 11:
            c = input('请输入短信验证码：')
            d = len(c)
            if d == 6:
                password1 = input('请输入密码：')
                password2 = input('请再次输入密码：')
                if password1 == password2 and len(password1) <= 8:
                    print('恭喜你，注册成功')

                else:
                    print('两次密码输入不一致或设置密码过短，请重新注册')
            else:
                print('短信验证码输入有误，请重新输入')
        else:
            print('手机输入错误，请重新输入')
    elif a == 3:
        break
