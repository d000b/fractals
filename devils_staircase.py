import numpy as np
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def devilsStaircase(ax):
    for i in range (0, 10):
        print(np.base_repr(i, 3))
    # ax.fill(x_coords, y_coords, color="white")


if __name__ == "__main__":
    ax, fig = initFigure()
    devilsStaircase(ax)
    plt.show()