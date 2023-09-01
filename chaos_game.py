import matplotlib.pyplot as plt
import numpy as np

POLYGON_X_COORDS = [0, 0.5, 1]
POLYGON_Y_COORDS = [0, np.sin(np.radians(60)) * 1, 0]


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    polyX = POLYGON_X_COORDS.copy()
    polyX.append(POLYGON_X_COORDS[0])
    polyY = POLYGON_Y_COORDS.copy()
    polyY.append(POLYGON_Y_COORDS[0])
    ax.plot(polyX, polyY, color='white', linewidth=2)
    return ax


def chaosGame(polygon, constant, iterations, ax):
    Rx, Ry = np.random.random(), np.random.random()

    while not isPointInsideTriangle([Rx, Ry], [0, 0, 0.5, np.sin(np.radians(60)) * 1, 1, 0]):
        Rx, Ry = np.random.random(), np.random.random()

    for i in range(0, iterations):
        randomVertice = np.random.randint(0, polygon)
        new_point = moveTowardsVertex([Rx, Ry], [POLYGON_X_COORDS[randomVertice], POLYGON_Y_COORDS[randomVertice]], constant)
        ax.scatter(new_point[0], new_point[1], color='purple', marker='o', s=1)
        Rx, Ry = new_point[0], new_point[1]


def isPointInsideTriangle(point, triangle):
    Ax, Ay, Bx, By, Cx, Cy = triangle
    Px, Py = point
    u = ((By - Cy) * (Px - Cx) + (Cx - Bx) * (Py - Cy)) / ((By - Cy) * (Ax - Cx) + (Cx - Bx) * (Ay - Cy))
    v = ((Cy - Ay) * (Px - Cx) + (Ax - Cx) * (Py - Cy)) / ((By - Cy) * (Ax - Cx) + (Cx - Bx) * (Ay - Cy))
    w = 1 - u - v
    return 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1


def moveTowardsVertex(point, vertex, fraction):
    Px, Py = point
    Vx, Vy = vertex
    Qx = (Px + Vx) * fraction
    Qy = (Py + Vy) * fraction
    return (Qx, Qy)


if __name__ == '__main__':
    ax = initFigure()
    chaosGame(3, 0.5, 5000, ax)
    plt.show()
