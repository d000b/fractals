import matplotlib.pyplot as plt
import numpy as np


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig


def calculate(m, a, point):
    dot = np.dot(m, point)
    return dot + a

if __name__ == '__main__':
    ax, fig = initFigure()

    p0 = np.array((0, 0))

    transformMatrices = [
        np.array(([0, 0], [0, 0.16])),
        np.array(([0.85, 0.04], [-0.04, 0.85])),
        np.array(([0.2, -0.26], [0.23, 0.22])),
        np.array(([-0.15, 0.28], [0.26, 0.24]))
    ]

    translationMatrices = [
        np.array((0, 0)),
        np.array((0, 1.6)),
        np.array((0, 1.6)),
        np.array((0, 0.44))
    ]

    x_points = [0]
    y_points = [0]

    for i in range(100_000):
        draw = np.random.choice([0, 1, 2, 3], 1, p=[0.01, 0.85, 0.07, 0.07])[0]
        p0 = calculate(transformMatrices[draw], translationMatrices[draw], p0)
        x_points.append(p0[0])
        y_points.append(p0[1])
    ax.scatter(x_points, y_points, color="green", s=0.01)
    plt.show()
