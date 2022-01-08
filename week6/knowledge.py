# 知识点
# 集合中每个元素都是唯一且无序的，集合中的元素不可更改，元素间用逗号隔开
def main():
    A = {"python", 123, ("python", 123), '1', 3}  # 使用{}建立集合
    B = set("pypy123")  # 使用set()建立集合，这里只有5个元素，1，2，3，p，y
    print(A)
    print(B)
    print(A|B)  # 返回一个新集合，包含集合A和B中所有的元素
    print(A&B)  # 返回一个新集合，包含集合在A与B中的元素
    print(A-B)  # 返回一个新集合，包括在A中却不在B中
    print(A^B)  # 返回一个新集合，包括在集合A和B中的非相同元素
    print(A>=B)  # 返回ture或者false，判断A和B的包含关系
    for item in A:
        print(item, end="")
    A.pop()  # 随即返回S的一个元素，更新A,若A为空，产生异常
if __name__ == '__main__':
    main()



# 数据去重
A = ["python", 123, ("python", 123), '1', 3, 123]
s = set(A)  # 利用集合无重复元素特点
m = list(s)  # 集合变列表（做到去重）


# 序列类型：字符串、元组、列表
ls = ['python', 123, 'io']
ls[::-1]  # 将列表逆序输出
s = "python123.io"
s[::-1]  # 字符串逆序输出



# 元组类型定义
creature = "dog", "tiger", "human", "cat"  # 一个等号后面接多个字符串
print(creature)
creature[::-1]  # 将元组逆序输出
color = (0x001100, "blue", creature)
print(color)



# 列表类型的操作
ls[i] = x  # 列表第i个元素替换为x
del ls[i]  # 删除列表第i个元素
ls.append(x)  # 列表ls后增加一个元素s
ls.clear()  # 列表清空
ls.reverse()  # 列表元素反转
ls += [1,2,3,4,5]  # 在列表中新增5个元素
ls.index(0)  # 返回数字0所在索引



# 字典是键值对的集合，键值对之间无序，采用{}或dict()创建，应用在映射表达中，比如统计数据
d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
d.keys()  # 返回索引
d.values()  # 返回值
d.get("中国", "湾湾")  # （k,<default>）键K存在，返回对应值，否则返回默认值
