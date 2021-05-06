import turtle

pen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#cccac4")

flag_color = "#e30a18"
pen.color(flag_color)
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
pen.color("white")
r=100
pen.circle(r)
pen.end_fill()

pen.penup()
pen.goto(5, 50)
pen.pendown()

#innercircle
pen.begin_fill()
pen.color(flag_color)
r=(0.4*400)/2
pen.circle(r)
pen.end_fill()

pen.penup()
pen.goto(-155 + 400 / 3, 50)
pen.pendown()

#star
pen.color("white")
pen.begin_fill()
pen.right(72)
pen.begin_fill()
for i in range(5):
    pen.forward(105.1462)
    pen.right(144)
pen.end_fill()

turtle.done()

