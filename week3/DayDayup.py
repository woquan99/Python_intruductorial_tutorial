# # 每天进步1%和退步1%的区别：
# dayup = pow(1.001, 365)
# daydown = pow(0.999, 365)
# print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
#
# # 一年365天，工作日进步1%，双休日每天退步1%：
# daystart = 1.0
# dayfactor = 0.001
# for i in range(365):
#     if i % 7 in [6, 0]:
#         daystart = daystart*(1-dayfactor)
#     else:
#         daystart = daystart*(1+dayfactor)
# print("工作日的力量：{:.2f}".format(daystart))

# 只知道周末会退步0.001，那么工作日该如何努力才能达到和每天都进步0.0001相同的效果呢？
def dayUP(df):
    daystart = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            daystart = daystart*(1-0.001)
        else:
            daystart = daystart*(1+df)
        return daystart
dayfactor=0.0001
while dayUP(dayfactor) < 1.44:
    dayfactor += 0.0001
print("工作日需要努力的参数是：{:.4f}".format(dayfactor))

# GRIT:perseverance and passion for long-term goals
