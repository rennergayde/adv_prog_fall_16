import turtle

window = turtle.Screen()

flower = turtle.Turtle()

flower.speed(100)

for i in range(360):
    flower.circle(75)
    flower.right(90)
    flower.circle(75)
    flower.right(90)
    flower.circle(75)
    flower.right(90)
    flower.circle(75)

    flower.penup()
    flower.setposition(0,0)
    flower.pendown()

    flower.right(1)


window.exitonclick()
