# 可变参数传递
def fact(n, *b):  # 含有*表示可变参数
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s
print(fact(10, 3))
print(fact(10, 3, 5, 8))


# 函数的返回值
def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m, n, m
a, b, c = fact(10, 5)  # 返回的数值为元组类型
print(a, b, c)


# 局部变量和全局变量
n, s = 10, 100
def fact(n):
    global s  # 可通过global保留字在函数内部声明全局变量
    for i in range(1, n+1):
        s *= i
    return s
print(fact(n), s)  # 此处全局变量s已经被修改


# 局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F", "f"]
def func(a):
    ls.append(a)
    return
func("C")
print(ls)
# 对比：
ls = ["F", "f"]
def func(a):
    ls = []  # 这里的局部变量被真实创建了
    ls.append(a)
    return
func("C")  # 这里只有局部变量ls被修改
print(ls)


# 递归的实现
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


# 将字符串s反转后输出
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs('yingzongquan'))


# 斐波那契数列
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)


# 汉诺塔
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(3, "A", "C", "B")
print(count)

