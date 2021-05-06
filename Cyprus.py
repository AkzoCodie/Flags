import turtle

pen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#cccac4")

flag_color_red = "#e30a18"
flag_color_white = "#ffffff"
pen.color(flag_color_white)
pen.hideturtle()

pen.penup()
pen.goto(-300, 250)
pen.pendown()

#mainsquare
pen.begin_fill()
pen.forward(600)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(600)
pen.right(90)
pen.forward(400)
pen.end_fill()

pen.penup()
pen.goto(0, 50)
pen.pendown()

#outercircle
pen.begin_fill()
pen.color(flag_color_red)
r=100
pen.circle(r)
pen.end_fill()

pen.penup()
pen.goto(5, 50)
pen.pendown()

#innercircle
pen.begin_fill()
pen.color(flag_color_white)
r=(0.4*400)/2
pen.circle(r)
pen.end_fill()

pen.penup()
pen.goto(-155 + 400 / 3, 50)
pen.pendown()

#star
pen.color(flag_color_red)
pen.begin_fill()
pen.right(72)
pen.begin_fill()
for i in range(5):
    pen.forward(105.1462)
    pen.right(144)
pen.end_fill()

pen.right(18)

pen.penup()
pen.goto(-300, 210)
pen.pendown()

pen.color(flag_color_red)
pen.begin_fill()
for i in range(2):
    pen.forward(600)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(-300, -70)
pen.pendown()

pen.begin_fill()
for i in range(2):
    pen.forward(600)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(-300-(400/30), 250)
pen.pendown()

pen.color(flag_color_white)
pen.begin_fill()
for i in range(2):
    pen.forward(400/30)
    pen.right(90)
    pen.forward(400)
    pen.right(90)
pen.end_fill()

turtle.done()