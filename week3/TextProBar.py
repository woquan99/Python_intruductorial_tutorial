# # 原始版：多行进度条
# import time
# scale = 10
# print("{0:*^30}".format("执行开始"))
# for i in range(scale+1):
#     a = '*' * i
#     b = '.' * (scale-i)
#     c = (i/scale) * 100
#     print("{:^3.0f}%[{}->{}]".format(c, a, b))
#     time.sleep(0.1)
# print("{0:*^30}".format("执行结束"))


# # 进阶版：单行进度条
# import time
# scale = 50
# print("\n{0:*^30}".format("执行开始"))
# start = time.perf_counter()
# for i in range(scale+1):
#     a = '*' * i
#     b = '.' * (scale-i)
#     c = (i/scale) * 100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end=" ")
#     time.sleep(0.1)
# print("\n{0:*^30}".format("执行结束"))


