# 列表便利循环
for item in [123, "PY", 456]:
    print(item, end=" ")

# 字符串遍历循环：
print('\n')
for c in "Python123":
    print(c, end=" ")

# break是跳出并结束当前整个循环，执行循环后的语句；
# continue则是结束当次循环，继续执行后续次数循环


# 循环控制保留字
print('\n')
s = "Python"
while s != "":
    for c in s:
        print(c, end="")
    s = s[:-1]

print('\n')
s = "JAVA"
while s != "":
    for c in s:
        if c == "V":
            break  # break仅跳出当前最内层循环
        print(c, end="")
    s = s[:-1]


# 基本随机数函数
import random
print('\n')
random.seed(1)  # 产生种子1对应的序列
print(random.random())  # 生成[0.0,1.0]之间的随机小数
print(random.random())
random.seed(1)
print(random.random())
print(random.randint(10, 100))  # 输出[a,b]之间的整数
print(random.randrange(10, 100, 10))  # [a,b,k]表示在[a,b]输出以步长k的随机整数
print(random.uniform(10, 100))  # 表示在[a,b]中输出随机小数
print(random.choice([1, 3, 56, 66, 43, 364, 363]))  # 表示在序列中输出随机选择一个元素
s = [1, 3, 56, 66, 43, 364, 363]
random.shuffle(s)
print(s)  # 将seq中元素随机排列，返回打乱后的序列
