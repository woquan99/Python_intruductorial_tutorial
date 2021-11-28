#%%
# import turtle
# turtle.pencolor("red")
# turtle.pensize(10)
# for i in range(6):
#     turtle.fd(40)
#     turtle.left(60)
# turtle.done()

#%%
# Draw overlapping polygons绘制叠变形，内角100°
# import turtle
# turtle.pencolor("green")
# turtle.pensize(5)
# for i in range(7):
#     turtle.fd(200)
#     turtle.left(100)
# turtle.done()

#%%
# Draw windmill绘制风车
import turtle
turtle.pensize(5)
for i in range(4):
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150, -45)
    turtle.goto(0, 0)
    turtle.left(45)
turtle.done()
