import math
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def cantorSet(ax, x_start, y_start, length, width, iterations):
    if iterations >= 10:
        return

    iterations += 1
    x_coords = [x_start, x_start + length, x_start + length, x_start, x_start]
    y_coords = [y_start, y_start, y_start + width, y_start + width, y_start]
    ax.fill(x_coords, y_coords, color="white")
    cantorSet(ax, x_start, y_start + width * 2, length / 3, width, iterations)
    cantorSet(ax, x_start + length * 2/3, y_start + width * 2, length / 3, width, iterations)


if __name__ == "__main__":
    ax, fig = initFigure()
    cantorSet(ax, 0, 0, 1, 0.05, 0)
    plt.show()