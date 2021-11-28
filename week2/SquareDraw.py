import turtle
turtle.pencolor("black")
## 法一
# turtle.fd(40)
# turtle.seth(90)
# turtle.fd(40)
# turtle.seth(180)
# turtle.fd(40)
# turtle.seth(270)
# turtle.fd(40)
## 法二：
for i in range(4):
    turtle.fd(40)
    turtle.left(90)
turtle.done()