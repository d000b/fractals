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

def devilsStaircase(ax, x_start, y_start, length, y_prev, width, iterations):
    if iterations >= 4:
        return
    iterations += 1

    print(x_start, y_start)
    
    if y_prev > 0.5:
        y_start = y_start
    else:
        y_start = y_start / 2

    x_coords = [x_start, x_start + length, x_start + length, x_start, x_start]
    y_coords = [y_start, y_start, y_start + width, y_start + width, y_start]

    print("aaaa new")
    print(x_start, y_start)
    print("----------")

    ax.fill(x_coords, y_coords, color="white")
    devilsStaircase(ax, x_start - 2 * length / 3, y_start / 2, length / 3, y_start, width, iterations)
    devilsStaircase(ax, x_start + length + length / 3, y_start * 2, length / 3, y_start, width, iterations)


if __name__ == "__main__":
    ax, fig = initFigure()
    # cantorSet(ax, 0, 0, 1, 0.05, 0)
    x_start = 0.333
    devilsStaircase(ax, x_start, 0.5, x_start, x_start, 0.05, 1)
    plt.show()