import turtle # 导入标准库
turtle.colormode(255) # RGB整数值模式 （1.0）为小数值
turtle.setup(650, 350, 200, 200) # 窗口长、宽、距离左上角的位置坐标
turtle.penup() # 画笔提起，只移动，不显示
turtle.fd(-250) # 朝海龟正前方移动
turtle.pendown()
turtle.pensize(20) # 别名turtle.width(width)
turtle.pencolor("green") # 可以使用RGB的小数值（0.63，0.13，0.94）
turtle.seth(-40) # 只改变海龟行进方向，向右下方转动40°
for i in range(4):
    turtle.circle(40, 80) # (r,angle)以左侧某点为圆心（半径为r），转动angle角
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
