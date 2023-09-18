# https://en.wikibooks.org/wiki/Fractals/Apollonian_fractals
import matplotlib.pyplot as plt
import matplotlib
import math
import numpy as np

colormap = matplotlib.colormaps.get_cmap('Greys')
# colormap = matplotlib.colormaps.get_cmap('turbo')


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')
    ax.set_aspect('equal')
    ax.margins(0)
    ax.autoscale()
    fig.patch.set_facecolor('black')
    return ax, fig


def drawCircle(ax, color, C):
    circle = plt.Circle(C[0], 1 / C[1], color=color, fill=False)
    ax.add_patch(circle)


def calculateThirdCircle(C1, r1, r2, r3):
    a = r1 + r2
    b = r1 + r3
    c = r3 + r2

    area = calculateAreaHerons(a, b, c)
    height = calculateHeightFromArea(area, a)
    C = calculateThirdCenter(b, height, C1[0])
    return (C, 1 / r3)


def calculateAreaHerons(a, b, c):
    sp = (a + b + c) / 2 # semiperimeter
    return math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))


def calculateHeightFromArea(area, base):
    return 2 * area / base


def calculateThirdCenter(hip, height, point):
    segment = math.sqrt(hip ** 2 - height ** 2)
    return (point[0] + segment, point[1] + height)


def descartesTheoremPositive(k1, k2, k3):
    k4 = k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    return k4


def descartesTheoremNegative(k1, k2, k3):
    k4 = k1 + k2 + k3 - 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    return k4


def complexDescartesTheoremPositive(C1, C2, C3, k4):
    z1 = C1[0][0] + 1j * C1[0][1]
    z2 = C2[0][0] + 1j * C2[0][1]
    z3 = C3[0][0] + 1j * C3[0][1]
    k1 = C1[1]
    k2 = C2[1]
    k3 = C3[1]

    z4 = (z1 * k1 + z2 * k2 + z3 * k3 + 2 * np.sqrt(k1 * k2 * z1 * z2 + k2 * k3 * z2 * z3 + k1 * k3 * z1 * z3)) / k4
    return (z4.real, z4.imag)


def complexDescartesTheoremNegative(C1, C2, C3, k4):
    z1 = C1[0][0] + 1j * C1[0][1]
    z2 = C2[0][0] + 1j * C2[0][1]
    z3 = C3[0][0] + 1j * C3[0][1]
    k1 = C1[1]
    k2 = C2[1]
    k3 = C3[1]

    z4 = (z1 * k1 + z2 * k2 + z3 * k3 - 2 * np.sqrt(k1 * k2 * z1 * z2 + k2 * k3 * z2 * z3 + k1 * k3 * z1 * z3)) / k4
    return (z4.real, z4.imag)


def fpp(C1, C2, C3):
    k4 = descartesTheoremPositive(C1[1], C2[1], C3[1])
    return (complexDescartesTheoremPositive(C1, C2, C3, k4), k4)


def fpm(C1, C2, C3):
    k4 = descartesTheoremPositive(C1[1], C2[1], C3[1])
    return (complexDescartesTheoremNegative(C1, C2, C3, k4), k4)


def fmm(C1, C2, C3):
    k4 = descartesTheoremNegative(C1[1], C2[1], C3[1])
    return (complexDescartesTheoremNegative(C1, C2, C3, k4), k4)


def fmp(C1, C2, C3):
    k4 = descartesTheoremNegative(C1[1], C2[1], C3[1])
    return (complexDescartesTheoremPositive(C1, C2, C3, k4), k4)


def apollonianGasket(ax, iterations, c1, c2, c3):
    if iterations == 0:
        return
    
    ck = fpp(c1, c2, c3)
    drawCircle(ax, colormap(iterations / its), ck)
    apollonianGasket(ax, iterations - 1, c1, c2, ck)
    apollonianGasket(ax, iterations - 1, c3, c2, ck)
    apollonianGasket(ax, iterations - 1, c1, c3, ck)


if __name__ == "__main__":
    its = 7

    # Soordinates should be well over > 0 (first quadrant)
    # Circle consists of center coordinates and curvature

    r1, r2, r3 = 3, 3, 3
    C1 = ((10, 0), 1 / r1)
    C2 = ((16, 0), 1 / r2)
    
    # r1, r2, r3 = 3, 5, 3
    # C1 = ((10, 0), 1 / r1)
    # C2 = ((18, 0), 1 / r2)
    
    # r1, r2, r3 = 10, 3, 3
    # C1 = ((100, 0), 1 / r1)
    # C2 = ((113, 0), 1 / r3)

    C3 = calculateThirdCircle(C1, r1, r2, r3)

    ax, fig = initFigure()
    drawCircle(ax, colormap(0), C1)
    drawCircle(ax, colormap(0), C2)
    drawCircle(ax, colormap(0), C3)

    ck_0out = fmm(C1, C2, C3) # change to fpp for an inverted effect
    ck_0in = fpp(C1, C2, C3)

    drawCircle(ax, colormap(0), ck_0out)
    drawCircle(ax, colormap(0), ck_0in)

    apollonianGasket(ax, its, C3, C2, ck_0out)
    apollonianGasket(ax, its, C1, C2, ck_0out)
    apollonianGasket(ax, its, C1, C3, ck_0out)
    apollonianGasket(ax, its, C3, C2, ck_0in)
    apollonianGasket(ax, its, C2, C1, ck_0in)
    apollonianGasket(ax, its, C1, C3, ck_0in)

    plt.show()
