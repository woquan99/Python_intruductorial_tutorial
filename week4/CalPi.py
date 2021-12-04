# # 利用圆周率的公式进行计算
# pi = 0
# N = 100
# for i in range(N):
#     pi += 1/pow(16, i) * (4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+ 6))
# print("圆周率Pi的数值为：{:.15f}".format(pi))
#
# # 利用蒙特卡罗方法进行计算
# from random import random
# from time import perf_counter
# hex = 1000*1000
# hit = 0
# start = perf_counter()
# for i in range(hex+1):
#     x, y = random(), random()
#     s = pow((pow(x, 2)+pow(y, 2)), 0.5)
#     if s <= 1:
#         hit += 1
# pi = (hit/hex)*4
# print("圆周率Pi的数值为{:.15f}".format(pi))
# print("程序耗时：{:.5f}s".format(perf_counter()-start))

# test
# 请以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。
from random import *   # import* 是导入了random模块的每个类，可以直接使用类，无需句点表示法
seed(123)
s = eval(input())
hit = 0
for i in range(s+1):
    x, y = random(), random()
    d = pow(pow(x, 2)+pow(y, 2), 0.5)
    if d <= 1:
        hit += 1
pi = (hit/s)*4
print("{:.6f}".format(pi))

