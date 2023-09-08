import turtle


def dragonCurve(turtle, iterations, length=1):
    if iterations == 0:
        turtle.forward(length)
    else:
        dragonCurve(turtle, iterations - 1, length)
        turtle.right(90)
        dragonCurveReverse(turtle, iterations - 1, length)

def dragonCurveReverse(turtle, iterations, length=200):
    if iterations == 0:
        turtle.forward(length)
    else:
        dragonCurve(turtle, iterations - 1, length)
        turtle.left(90)
        dragonCurveReverse(turtle, iterations - 1, length)


if __name__ == "__main__":

    screen = turtle.Screen()
    screen.setup(1000, 1000)
    screen.bgcolor("black")

    dragon = turtle.Turtle()
    dragon.speed(0)
    dragon.color("white")
    
    dragon.penup()
    dragon.goto(100, 0)
    dragon.pendown()

    dragonCurve(dragon, 20)

    turtle.done()
