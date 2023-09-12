import math
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def drawCircle(ax, c, r):
    circle = plt.Circle(c, r, color='white', fill=False)
    ax.add_patch(circle)

def calculateTriangleSides(C1, C2, C3):
    a = math.dist(C1, C2)
    b = math.dist(C2, C3)
    c = math.dist(C1, C3)
    return a, b, c

def inCircleRadius(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt((s * (s - a) * (s - b) * (s - c)) / s ** 2)

    

if __name__ == "__main__":
    ax, fig = initFigure()
    
    # Initial three circles
    C1, C2, C3 = (-3, 2), (0, -5), (3, 2)
    R1, R2, R3 = 2, 0, 0


    a, b, c = calculateTriangleSides(C1, C2, C3)
    x = inCircleRadius(a, b, c)

    R3 = c - R1 - R2
    R2 = a - R1 - R3


    drawCircle(ax, C1, R1)
    drawCircle(ax, C2, R2)
    drawCircle(ax, C3, R3)
    plt.show()