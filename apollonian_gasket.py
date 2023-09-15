import matplotlib.pyplot as plt
import numpy as np
import math


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')
    ax.set_aspect('equal')

    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)


    fig.patch.set_facecolor('black')
    return ax, fig


def drawCircle(ax, c, r):
    circle = plt.Circle(c, r, color='white', fill=False)
    ax.add_patch(circle)


def calculateThirdCircle(C1, C2, R1, R2, R3):
    a = R1 + R2
    b = R1 + R3
    c = R3 + R2

    area = calculateAreaHerons(a, b, c)
    height = calculateHeightFromArea(area, a)
    C = calculateThirdCenter(b, height, C1)
    return C


def calculateAreaHerons(a, b, c):
    # semiperimeter
    sp = (a + b + c) / 2
    return math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))


def calculateHeightFromArea(area, base):
    return 2 * area / base


def calculateThirdCenter(hip, height, point):
    segment = math.sqrt(hip ** 2 - height ** 2)
    return (point[0] + segment, point[1] + height)


def descartesTheorem(R1, R2, R3):
    denominator = R1 * R2 + R2 * R3 + R3 * R1
    common_term = 2 * math.sqrt(R1 * R2 * R3 * (R1 + R2 + R3))
    
    Xinterior = R1 * R2 * R3 / (denominator + common_term)
    Xexterior = R1 * R2 * R3 / (denominator - common_term)
    
    return Xinterior, abs(Xexterior)


if __name__ == "__main__":
    ax, fig = initFigure()
    
    # Distance between A and B should make up to R1 + R2
    # A, B = (-3, 0), (3, 0)
    # R1, R2, R3 = 3, 3, 3
    A, B = (-3, 0), (5, 0)
    R1, R2, R3 = 3, 5, 3

    C = calculateThirdCircle(A, B, R1, R2, R3)

    R4_i, R4_e = descartesTheorem(R1, R2, R3)
    print(R4_i, R4_e)

    drawCircle(ax, A, R1)
    drawCircle(ax, B, R2)
    drawCircle(ax, C, R3)
    plt.show()