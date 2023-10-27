import turtle


def decimalFractionToTernaryFraction(decimal, precision=10):
    result = "0."

    for _ in range(precision):
        decimal *= 3
        digit = int(decimal)
        result += str(digit)
        decimal -= digit

    return result

def binaryFractionToDecimalFraction(binaryFraction):
    decimalFraction = 0.0
    for i, bit in enumerate(binaryFraction[2:]):
        decimalFraction += int(bit) * (2 ** -(i + 1))
    return decimalFraction

# https://en.wikipedia.org/wiki/Cantor_function
def cantorFunction(x):
    numberString = decimalFractionToTernaryFraction(x)
    
    firstOneIndex = numberString.find("1")
    if firstOneIndex != -1:
        numberString = numberString[:firstOneIndex + 1] + "0" * (len(numberString) - firstOneIndex - 1)

    numberString = numberString.replace("2", "1")
    return float(binaryFractionToDecimalFraction(numberString))

def devilsStaircase(limit):
    x = []
    y = []
    for i in range(0, limit):
        n = i / (limit)
        c = cantorFunction(n)
        x.append(n)
        y.append(c)
    return x, y

def drawDevilsStaircase(xCoords, yCoords):
    window = turtle.Screen()
    window.bgcolor("black")
    turtle.setworldcoordinates(0, 0, 1, 1)
    
    turt = turtle.Turtle()
    turt.color("white")
    turt.speed(100)
    turt.penup()
    turt.goto(0, 0)
    turt.width(3)
    turt.pendown()

    for x, y in zip(xCoords, yCoords):
        turt.goto(x, y)

    window.exitonclick()

if __name__ == "__main__":

    x, y = devilsStaircase(1000)
    drawDevilsStaircase(x, y)
