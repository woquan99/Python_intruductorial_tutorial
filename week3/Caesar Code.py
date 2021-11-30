code = input()
encode = ""
for c in code:
    if 'a' <= c <= 'z':
        encode += chr(ord('a') + ((ord(c)-ord('a')) + 3) % 26)
        # chr()函数用于从给定的ASCII码 (整数值)中获取字符值，它接受一个数字(应为ASCII码 )并返回字符
        # ord（）函数就是用来返回单个字符的ascii值（0-255）或者unicode数值（）
    elif 'A' <= c <= 'Z':
        encode += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
    else:
        encode += c
print(encode)


