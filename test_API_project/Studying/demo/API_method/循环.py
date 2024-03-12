# !/user/bin/env python3
# -*- coding: utf-8 -*-
# 思考：假如我有个女朋友，有一天我们闹矛盾生气了，女朋友说：道歉，说100遍“媳妇儿，我错了”。这个时候程序员会怎么做？
i = 1
sum = 0
while i < 10:
    print("媳妇儿，我错了")
    i +=1
    print(i)
print("道歉完成")

# 应用一：计算1-100累加和
i = 1
result = 0
while i <= 100:
    result +=i
    i+=1
    print(result)

# 应用二：计算1-100偶数累加和
i=1
result = 0
while i <=100:
    if i % 2 ==0:
        result +=i
    i+=1
print(result)

# 如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第五个苹果
i = 1
while i <=5:
    if i ==4:
        print("次饱了，不想次了")
        break
    print(f'吃了{i}个苹果')
    i +=1

# 吃到第三个吃出一个大虫子
i = 1
while i <= 5:
    if i == 3:
        print(f"吃到了{i}有虫子")
        i += 1
        continue
    print(f'吃了{i}个苹果')
    i += 1

# 有天女朋友又生气了，惩罚：说3遍“媳妇儿， 我错了”，这个程序是不是循环即可？但如果女朋友说：还要刷今天晚饭的碗，这个程序怎么书写？
t = 1
while t <= 3:
    print('媳妇我错了')
    t += 1
print('刷今天的碗')

# 但如果女朋友还是生气，把这套惩罚要连续3天都执行，有如何书写程序？
l = 1
while l <= 3:
    t = 1
    while t <= 3:
        print('媳妇我错了')
        t += 1
    print("刷今天的碗")
    print('-----惩罚结束------')
    l += 1

# 九九乘法表格
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f'{i}*{j}={i*j}',end='\t')
        j += 1
    print()
    i += 1

# for 循环
str1 = 'python'
for i in str1:
    print(i)
# 遇到h不打印
str1 = 'python'
for i in str1:
    if i == 'h':
        print('遇到h不打印')
        break
    print(i)
# 遇到h不打印，然后继续打印
str1 = 'python'
for i in str1:
    if i =="h":
        print(f'遇到{i}不打印，然后继续打印')
        continue
    print(i)

# 需求：女朋友生气了，要惩罚：连续说5遍“媳妇儿，我错了”，如果道歉正常完毕女朋友就原谅我了，这个程序怎么写？
t = 1
while t <= 5:
    print('媳妇我错了')
    t += 1
else:
    print('媳妇原谅我啦真开心')

# 退出循环的方式
# 需求：女朋友生气，要求道歉5遍：媳妇儿，我错了。道歉到第三遍的时候，媳妇埋怨这一遍说的不真诚，是不是就是要退出循环了？这个退出有两种可能性：
# 更生气，不打算原谅，也不需要道歉了，程序如何书写？
# 只一遍不真诚，可以忍受，继续下一遍道歉，程序如何书写？
t = 1
while t <= 5:
    if t ==3:
        print('这遍不真诚，滚犊的')
        break
    t += 1
    print('媳妇我错了')

t = 1
while t <= 5:
    if t == 3:
        print('这边不真诚，滚犊的')
        t += 1
        continue
    print("媳妇我错了")
    t += 1
else:
    print('媳妇原谅我啦真开心')

# for else循环
str1 = 'python'
for i in str1:
    if i == 'h':
        print(f'遇到{i}不打印')
        break
    print(i)
else:
    print("继续执行下一段代码")

str1 = 'python'
for i in str1:
    if i == 'h':
        print(f'遇到{i}不打印')
        continue
    print(i)
else:
    print("继续执行下一段代码")

# 总结
# 循环的作用：控制代码重复执行
# while语法
# while 条件:
#     条件成立重复执行的代码1
#     条件成立重复执行的代码2
#     ......

# while循环嵌套语法
# while 条件1:
#     条件1成立执行的代码
#     ......
#     while 条件2:
#         条件2成立执行的代码
#         ......

# for循环语法
# for 临时变量 in 序列:
#     重复执行的代码1
#     重复执行的代码2
#     ......

# break退出整个循环
# continue退出本次循环，继续执行下一次重复执行的代码

# else
# while和for都可以配合else使用
# else下方缩进的代码含义：当循环正常结束后执行的代码
# break终止循环不会执行else下方缩进的代码
# continue退出循环的方式执行else下方缩进的代码