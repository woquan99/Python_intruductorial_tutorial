TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ["F", "f"]:
    # eval获得一个字符串输入，会计算字符串中的表达式并返回结果
    C = (eval(TempStr[:-1])-32)/1.8
    # 保留小数点后三位
    print("转化后的温度为{:.3f}℃".format(C))
elif TempStr[-1] in ["C", "c"]:
    F = 1.8*eval(TempStr[:-1])+32
    # 保留小数点后两位
    print("转化后的温度为{:.2f}F".format(F))
else:
    print("输入格式有误")