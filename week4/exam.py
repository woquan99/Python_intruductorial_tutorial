'''
for var in ___:
    print(var)
哪个选项不符合上述程序空白处的语法要求？
A. range(0,10)
B. “Hello”
C. (1,2,3)
D. {1;2;3;4;5}

正确答案 D
for … in … 中 in 的后面需要是一个迭代类型（组合类型），{1;2;3;4;5}不是Python的有效数据类型。
'''


'''
哪个选项是random库中用于生成随机小数的函数？
A. randint()
B. random()
C. randrange()
D. getrandbits()

正确答案 B
randint()、getrandbits()、randrange()都产生随机整数，random()产生0到1之间的随机小数。

'''


'''
四位玫瑰数是4位数的自幂数。自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。
例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，3位数的自幂数被称为水仙花数。
请输出所有4位数的四位玫瑰数，按照从小到大顺序，每个数字一行
输入输出示例
输出仅表示格式，不表示对错。
'''
# 方法一（trash）
for i in range(1000, 10000):
    if (pow((i%10), 4)+pow(((i%100-i%10)/10), 4)+pow(((i%1000-i%100)/100), 4)+pow(((i-i%1000)/1000), 4)) == i:
        print(i,end="\n")

# 方法二：
s = ""
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4) + pow(eval(t[3]),4) == i :
        print(i, end="\n")


'''
求100以内所有素数之和并输出。
素数指从大于1，且仅能被1和自己整除的整数。
提示：可以逐一判断100以内每个数是否为素数，然后求和
'''
sum = 0
for i in range(2, 101):
    for k in range(2, i):
        if i%k==0:
            break
    else:
        sum += i
print(sum)