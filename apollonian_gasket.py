import matplotlib.pyplot as plt
import numpy as np
import math


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')
    ax.set_aspect('equal')

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)


    fig.patch.set_facecolor('black')
    return ax, fig


def drawCircle(ax, color, c, r):
    circle = plt.Circle(c, r, color=color, fill=False)
    ax.add_patch(circle)


def calculateThirdCircle(C1, r1, r2, r3):
    a = r1 + r2
    b = r1 + r3
    c = r3 + r2

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


def descartesTheorem(k1, k2, k3):
    k4_i = k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    k4_e = k1 + k2 + k3 - 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)

    return k4_i, k4_e


def complexDescartesTheorem(C1, C2, C3, k1, k2, k3, k4):
    z1 = C1[0] + 1j * C1[1]
    z2 = C2[0] + 1j * C2[1]
    z3 = C3[0] + 1j * C3[1]

    z4 = (z1 * k1 + z2 * k2 + z3 * k3 + 2 * np.sqrt(k1 * k2 * z1 * z2 + k2 * k3 * z2 * z3 + k1 * k3 * z1 * z3)) / k4
    z4_n = (z1 * k1 + z2 * k2 + z3 * k3 - 2 * np.sqrt(k1 * k2 * z1 * z2 + k2 * k3 * z2 * z3 + k1 * k3 * z1 * z3)) / k4
    print(f"z4:{z4} z4_n: {z4_n}")

    return (z4.real, z4.imag), (z4_n.real, z4_n.imag)


def apollonianGasket(ax, color, iterations, C1, C2, C3, r1, r2, r3, internal, index):
    if iterations == 0:
        return
    
    k1, k2, k3 = 1 / r1, 1 / r2, 1 / r3
    k4_i, k4_e = descartesTheorem(k1, k2, k3)
    r4_i, r4_e = 1 / k4_i, 1 / k4_e

    c4_1, c4_2 = complexDescartesTheorem(C1, C2, C3, k1, k2, k3, k4_i)
    c4_3, c4_4 = complexDescartesTheorem(C1, C2, C3, k1, k2, k3, k4_e)
    
    if internal:
        drawCircle(ax, color, c4_1, r4_i)
    else:
        drawCircle(ax, color, c4_2, r4_i)
    

    if index == 1:
        apollonianGasket(ax, "red", iterations - 1, C1, C2, c4_1, r1, r2, r4_i, True, index)
        apollonianGasket(ax, "red", iterations - 1, C2, C3, c4_1, r2, r3, r4_i, True, index)
        apollonianGasket(ax, "red", iterations - 1, C1, C3, c4_1, r1, r3, r4_i, False, index)

    #2 = #5
    if index == 2 or index == 5:
        apollonianGasket(ax, "green", iterations - 1, C1, C2, c4_1, r1, r2, r4_i, True, index)
        apollonianGasket(ax, "green", iterations - 1, C2, C3, c4_1, r2, r3, r4_i, True, index)
        apollonianGasket(ax, "green", iterations - 1, C1, C3, c4_1, r1, r3, r4_i, True, index)

    #3 = #6
    if index == 3 or index == 6:
        apollonianGasket(ax, "blue", iterations - 1, C1, C2, c4_2, r1, r2, r4_i, False, index)
        apollonianGasket(ax, "blue", iterations - 1, C2, C3, c4_2, r2, r3, r4_i, False, index)
        apollonianGasket(ax, "blue", iterations - 1, C1, C3, c4_2, r1, r3, r4_i, False, index)

    # 4
    if index == 4:
        apollonianGasket(ax, "purple", iterations - 1, C1, C2, c4_2, r1, r2, r4_i, False, index)
        apollonianGasket(ax, "purple", iterations - 1, C2, C3, c4_2, r2, r3, r4_i, True, index)
        apollonianGasket(ax, "purple", iterations - 1, C1, C3, c4_2, r1, r3, r4_i, False, index)


if __name__ == "__main__":
    ax, fig = initFigure()
    
    # Distance between A and B should make up to r1 + r2
    # C1, C2 = (-3, 0), (3, 0)
    # r1, r2, r3 = 3, 3, 3
    C1, C2 = (-3, 0), (5, 0)
    r1, r2, r3 = 3, 5, 3
    k1, k2, k3 = 1 / r1, 1 / r2, 1 / r3

    C3 = calculateThirdCircle(C1, r1, r2, r3)

    k4_i, k4_e = descartesTheorem(k1, k2, k3)
    r4_i, r4_e = 1 / k4_i, 1 / k4_e

    print(k4_i, k4_e)
    print(1 / k4_i, 1 / k4_e)

    c4_1, c4_2 = complexDescartesTheorem(C1, C2, C3, k1, k2, k3, k4_i)
    c4_3, c4_4 = complexDescartesTheorem(C1, C2, C3, k1, k2, k3, k4_e)

    drawCircle(ax, 'white', C1, r1)
    drawCircle(ax, 'white', C2, r2)
    drawCircle(ax, 'white', C3, r3)

    # for internal - first solution
    drawCircle(ax, 'white', c4_1, r4_i)
    # drawCircle(ax, 'purple', c4_2, r4_i)

    # for external -> second solution
    # drawCircle(ax, 'green', c4_3, r4_e)
    drawCircle(ax, 'white', c4_4, r4_e)

    print("-=-=-=-=-=-=-=-=-=-=-")
    iterations = 2
    apollonianGasket(ax, "white", iterations, C1, C2, c4_1, r1, r2, r4_i, True, 1)  #1
    apollonianGasket(ax, "white", iterations, C2, C3, c4_1, r2, r3, r4_i, True, 2)  #2
    apollonianGasket(ax, "white", iterations, C1, C3, c4_1, r1, r3, r4_i, False, 3) #3
    apollonianGasket(ax, "white", iterations, C1, C2, c4_4, r1, r2, r4_e, False, 4) #4
    apollonianGasket(ax, "white", iterations, C2, C3, c4_4, r2, r3, r4_e, True, 5)  #5
    apollonianGasket(ax, "white", iterations, C1, C3, c4_4, r1, r3, r4_e, False, 6) #6


    plt.show()
    