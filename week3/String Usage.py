
#%% 这一次的代码段涉及到字符串的一些基本应用

# Str = input("0123456789:")
# print(Str[::-1]) # 将输入的字符串倒序输出

# def Str1(test):
#     num = input()
#     if test in num:
#         print("yes")
#     else:
#         print("test不是num的子串")
# Str1("3") # 注意这里是字符串和字符串之间的比较，所以输入的“3”，而非3(int)

# WeekNamePrint.py
# weekStr = "一二三四五六日"
# weekId = eval(input("请输入星期数字（1——7）："))
# print("星期"+weekStr[weekId-1])

'''
len()返回字符串长度
str()返回所对应的字符串形式
hex(x)是整数x的十六进制，oct()则是八进制
'''

# 输出十二星座的图标
# for i in range(12):
#     print(chr(9800+i), end=" ")
import time
print("adeDged".lower())  # 字符小写
print("adeDged".upper())  # 字符大写
print("an apple a day".count("a"))  # 计算a的次数
print("python".replace("n", "n123.io"))  # 返回替换的字符串副本
print("python".center(30, "="))  # 用于制造输出的分割线
print("{0:*^30}".format("python"))  # ^表示中间对齐
print("{0:*>30}".format("python"))  # >表示右对齐
print("{0:*<30}".format("python"))  # <表示右对齐
print(",".join("123456"))  # 用于字符串分隔


# 时间格式化
start = time.perf_counter()
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))  # time转变为字符串
timeStr = '2021-11-29 19:31:21'
print(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))  # 字符串转变为time
time.sleep(3)  # 等待3s
end = time.perf_counter()
print("程序运行时间：", (end-start), "s")  # 程序运行计时

