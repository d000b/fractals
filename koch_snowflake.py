import math
import matplotlib.pyplot as plt

from regular_polygon_generator import calculatePolygonCoordinates


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig


def kochSnowflake(x_coords, y_coords, maxIterations, currentIteration, ax):

    if currentIteration >= maxIterations:
        ax.plot(x_coords, y_coords, color='white', linewidth=0.5)
        return
    currentIteration = currentIteration + 1

    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    new_x_coords = []
    new_y_coords = []

    for i in range(0, len(x_coords) - 1):
        new_x_coords.append(x_coords[i])
        new_y_coords.append(y_coords[i])

        d1_x, d1_y, d2_x, d2_y = divideInThreeParts(x_coords[i], y_coords[i], x_coords[i + 1], y_coords[i + 1])
        cx, cy = getTriangleCenterVertice(d1_x, d1_y, d2_x, d2_y)

        new_x_coords.append(d1_x)
        new_y_coords.append(d1_y)

        new_x_coords.append(cx)
        new_y_coords.append(cy)

        new_x_coords.append(d2_x)
        new_y_coords.append(d2_y)

    kochSnowflake(new_x_coords, new_y_coords, maxIterations, currentIteration, ax)


def divideInThreeParts(x1, y1, x2, y2):

    divider1_x = x1 + (x2 - x1) / 3
    divider1_y = y1 + (y2 - y1) / 3

    divider2_x = x1 + 2 * (x2 - x1) / 3
    divider2_y = y1 + 2 * (y2 - y1) / 3

    return divider1_x, divider1_y, divider2_x, divider2_y


def getTriangleCenterVertice(x1, y1, x2, y2):
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    third_vertex_x = center_x + (y2 - y1) * math.sin(math.radians(60))
    third_vertex_y = center_y + (x1 - x2) * math.sin(math.radians(60))

    return third_vertex_x, third_vertex_y


if __name__ == "__main__":
    x_coords, y_coords = calculatePolygonCoordinates(3)
    ax, fig = initFigure()
    kochSnowflake(x_coords, y_coords, 5, 0, ax)
    plt.show()
    