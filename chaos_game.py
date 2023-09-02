import matplotlib.pyplot as plt
import numpy as np

from regular_polygon_generator import calculatePolygonCoordinates
from matplotlib.backends.backend_agg import FigureCanvasAgg


def initFigure(x_coords, y_coords):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    polyX = x_coords.copy()
    polyX.append(x_coords[0])
    polyY = y_coords.copy()
    polyY.append(y_coords[0])
    ax.plot(polyX, polyY, color='white', linewidth=2)
    return ax, fig


def chaosGame(n, x_coords, y_coords, constant, iterations, ax):
    Rx, Ry = np.random.random(), np.random.random()

    while not isPointInsidePolygon([Rx, Ry], x_coords, y_coords):
        Rx, Ry = np.random.random(), np.random.random()

    for i in range(iterations):
        randomVertice = np.random.randint(0, n)
        new_point = moveTowardsVertex([Rx, Ry], [x_coords[randomVertice], y_coords[randomVertice]], constant)
        ax.scatter(new_point[0], new_point[1], color='blue', marker='o', s=0.5)
        Rx, Ry = new_point[0], new_point[1]


def isPointInsidePolygon(point, vertices_x, vertices_y):
    x, y = point
    n = len(vertices_x)
    inside = False

    for i in range(n):
        j = (i + 1) % n
        if (vertices_y[i] > y) != (vertices_y[j] > y) and \
           x < (vertices_x[j] - vertices_x[i]) * (y - vertices_y[i]) / (vertices_y[j] - vertices_y[i]) + vertices_x[i]:
            inside = not inside

    return inside


def moveTowardsVertex(point, vertex, fraction):
    Px, Py = point
    Vx, Vy = vertex
    Qx = Px + (Vx - Px) * fraction
    Qy = Py + (Vy - Py) * fraction
    return (Qx, Qy)


if __name__ == '__main__':
    n = 10
    POLYGON_X_COORDS, POLYGON_Y_COORDS = calculatePolygonCoordinates(n)
    ax, fig = initFigure(POLYGON_X_COORDS, POLYGON_Y_COORDS)

    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.5, 10000, ax) # 3
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.55, 10000, ax) # 4
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.66, 10000, ax) # 5
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.66, 10000, ax) # 6
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.66, 10000, ax) # 7
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.75, 10000, ax) # 8
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.75, 10000, ax) # 9
    # chaosGame(n, POLYGON_X_COORDS, POLYGON_Y_COORDS, 0.75, 10000, ax) # 10

    # plt.show()

    # Save as images
    fig_agg = FigureCanvasAgg(fig)
    fig_agg.figure.savefig('images/cg_' + str(n) + '.jpg', dpi=300)
