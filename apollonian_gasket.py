import math
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def drawInitialCircles(ax, c0, c1, c2, r0, r1, r2):
    outerCircle = plt.Circle(c0, r0, color='white', fill=False)
    circle1 = plt.Circle(c1, r1, color='white', fill=False)
    circle2 = plt.Circle(c2, r2, color='white', fill=False)
    ax.add_patch(outerCircle)
    ax.add_patch(circle1)
    ax.add_patch(circle2)

def drawCircle(ax, c, r):
    circle = plt.Circle(c, r, color='white', fill=False)
    ax.add_patch(circle)

def descartesTheorem(a, b, c):
    return a + b + c + 2 * (math.sqrt(a * b + b * c + c * a)),  a + b + c - 2 * (math.sqrt(a * b + b * c + c * a))



if __name__ == "__main__":
    ax, fig = initFigure()
    
    r0, r1, r2 = 1, 0.5, 0.5
    c0, c1, c2 = (0, 0), (-r1, 0), (r2, 0)
    drawInitialCircles(ax, c0, c1, c2, r0, r1, r2)

    # curvatures of each circle
    cu0 = -1 / r0
    cu1 = 1 / (r1)
    cu2 = 1 / (r2)
    # print(cu0, cu1, cu2)
    cuN = descartesTheorem(cu0, cu1, cu2)
    # print(cuN)
    cuN = cuN[0]
    rN = 1 / cuN
    drawCircle(ax, (0, -r0 + rN), rN)
    drawCircle(ax, (0, +r0 - rN), rN)


    cu4 = descartesTheorem(cuN, cu0, cu2)
    # print(cu4)
    cu4 = cu4[0]
    r4 = 1 / cu4
    drawCircle(ax, (0, -r0 + r4), r4)
    drawCircle(ax, (0, +r0 - r4), r4)

    plt.show()