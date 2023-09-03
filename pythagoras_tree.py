import matplotlib.pyplot as plt

def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-700, 700)
    ax.set_ylim(-100, 800)
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax

def drawPythagorasTree(ax, x1, y1, x2, y2, currentDepth, maxDepth):
    if currentDepth > 0:
        # Calculate the differences in x and y coordinates between the two points
        dx, dy = x2 - x1, y2 - y1

        # Calculate the coordinates for the three additional points to create the branches
        x3, y3 = x2 - dy, y2 + dx
        x4, y4 = x1 - dy, y1 + dx
        x5, y5 = x4 + (dx - dy) / 2, y4 + (dx + dy) / 2

        color_intensity = 1.0 - (currentDepth / maxDepth)
        color = (1.0, color_intensity, 1.0)

        ax.plot([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color=color)

        drawPythagorasTree(ax, x4, y4, x5, y5, currentDepth - 1, maxDepth)
        drawPythagorasTree(ax, x5, y5, x3, y3, currentDepth - 1, maxDepth)


if __name__ == '__main__':
    ax = initFigure()
    drawPythagorasTree(ax, -100, 0, 100, 0, 12, 12)
    plt.show()
