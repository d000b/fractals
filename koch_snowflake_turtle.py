import turtle


def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def draw_koch_snowflake(order, size):
    window = turtle.Screen()
    window.bgcolor("black")
    
    snowflake = turtle.Turtle()
    snowflake.color("white")
    snowflake.speed(100)
    snowflake.penup()
    snowflake.goto(-size / 2, size / 3)
    snowflake.pendown()

    for _ in range(3):
        koch_snowflake(snowflake, order, size)
        snowflake.right(120)

    window.exitonclick()

draw_koch_snowflake(4, 500)
