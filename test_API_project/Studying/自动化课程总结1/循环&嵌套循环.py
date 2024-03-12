M = int(input()) #获取房价
X = int(input()) #获取小明的年薪
sum = 0 # 小明手里的钱
age = 20 # 小明的年龄
while age < 80 and sum < M : # and 是并且的意思，在这里and可以判断左右两边的条件是否同时满足
    age = age + 1
    sum = sum + X
    X = X*1.08 # 工资的涨幅
    M = M*1.1  # 房价的涨幅
if(sum >= M):	# # 如果 sum >= M  则输出 小明在 age 岁的时候能买到房子
  print("小明在",age,"岁的时候能买到房子")
else:
  print("小明在有生之年买不到房子")