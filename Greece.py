import turtle

pen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#cccac4")

flag_color_blue = "#0D5EAF"
flag_color_white = "#ffffff"
total = 540
en = 360

x = -250
y = 250

pen.hideturtle()

pen.penup()
pen.goto(-250, 250)
pen.pendown()

pen.color(flag_color_blue)
pen.begin_fill()
for i in range(2):
    pen.forward(540)
    pen.right(90)
    pen.forward(360)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(-170, 250)
pen.pendown()

pen.color(flag_color_white)
pen.begin_fill()
for i in range(2):
    pen.forward(40)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(-250, 170)
pen.pendown()

pen.color(flag_color_white)
pen.begin_fill()
for i in range(2):
    pen.forward(200)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
pen.end_fill()

for i in range(2):
    pen.penup()
    pen.goto(x+200, y-40)
    pen.pendown()
    pen.color(flag_color_white)
    pen.begin_fill()
    for i in range(2):
        pen.forward(340)
        pen.right(90)
        pen.forward(40)
        pen.right(90)
    pen.end_fill()
    y-=80

x = -250
y = 250

for i in range(2):
    pen.penup()
    pen.goto(-250, y-200)
    pen.pendown()
    pen.color(flag_color_white)
    pen.begin_fill()
    for i in range(2):
        pen.forward(540)
        pen.right(90)
        pen.forward(40)
        pen.right(90)
    pen.end_fill()
    y -= 80

pen.penup()
pen.goto(-250, 250)
pen.pendown()

pen.color(flag_color_blue)
for i in range(2):
    pen.forward(540)
    pen.right(90)
    pen.forward(360)
    pen.right(90)

turtle.done()



