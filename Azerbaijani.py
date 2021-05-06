import turtle

p = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#cccac4")

flag_color_blue = "#00b5e2"
flag_color_red = "#ef3340"
flag_color_green = "#509e2f"
p.hideturtle()
a = 46.19393
b = 135

p.penup()
p.goto(-300, 250)
p.pendown()

#blue color flag
p.begin_fill()
for i in range(2):
    p.color(flag_color_blue)
    p.forward(600)
    p.right(90)
    p.forward(100)
    p.right(90)
p.end_fill()

p.penup()
p.goto(-300, 150)
p.pendown()

#red color flag
p.begin_fill()
for i in range(2):
    p.color(flag_color_red)
    p.forward(600)
    p.right(90)
    p.forward(100)
    p.right(90)
p.end_fill()

p.penup()
p.goto(-300, 50)
p.pendown()

#green color flag
p.begin_fill()
for i in range(2):
    p.color(flag_color_green)
    p.forward(600)
    p.right(90)
    p.forward(100)
    p.right(90)
p.end_fill()

p.penup()
p.goto(-15, 55)
p.pendown()

#outer circle
p.begin_fill()
p.color("white")
r=45
p.circle(r)
p.end_fill()

p.penup()
p.goto(-5, 62.5)
p.pendown()

#inner circle
p.begin_fill()
p.color(flag_color_red)
r=37.5
p.circle(r)
p.end_fill()

p.penup()
p.goto(35, 75)
p.pendown()

#8 pointed star
p.begin_fill()
p.color("white")
p.left(67.5)
for i in range(8):
    p.forward(a)
    p.left(b)
p.end_fill()

turtle.done()
