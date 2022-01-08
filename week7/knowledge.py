# 文本形式打开文件
tf = open("f.txt", encoding="utf-8").read()
bf = open("f.txt", "rb")
print(bf.readline())
# bf.readlines()  # 读入文件所有行，以每行行为元素形成列表
print(tf)
tf.close()
bf.close()

# python文件路径采用’/‘而非’\‘，或者使用’\\‘
f = open("f.txt", "rt")  # 只读模式
f = open("f.txt", "w")  # 覆盖写模式
f = open("f.txt", "a+")  # 追加写模式+读文件
f = open("f.txt", "x")  # 创建写模式
f = open("f.txt", "b")  # 二进制形式，只读模式


#
fo = open("output.txt", "w+")
ls = ["中国", "巴基斯坦"]
fo.writelines(ls)
for line in fo:
    print(line)  # 此时没有任何输出
fo.close()

# 对照组
fo = open("output.txt", "w+")
ls = ["中国", "巴基斯坦"]
fo.writelines(ls)
fo.seek(0)  # 回到文件开头
for line in fo:
    print(line)  # 此时没有任何输出
fo.close()