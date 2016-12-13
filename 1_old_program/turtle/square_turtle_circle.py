import turtle

window = turtle.Screen()

square = turtle.Turtle()

square.speed(10)

for i in range(360):
    square.forward(75)
    square.right(90)
    square.forward(75)
    square.right(90)
    square.forward(75)
    square.right(90)
    square.forward(75)

    square.penup()
    square.setposition(0,0)
    square.pendown()

    square.right(1)


window.exitonclick()
