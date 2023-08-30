import matplotlib.pyplot as plt
import numpy as np
import math

def calcHeight(length):
    return math.sin(math.radians(60)) * length

def calcHeight2(length):
    return math.cos(math.radians(60)) * length

def drawTriangle(ax, vertices, i):
    if i > 4:
        return
    i = i + 1

    vertices_left = np.array([vertices[0], [vertices[1][0] / 2, vertices[1][1] / 2], [vertices[2][0] / 2, vertices[2][1] / 2]])
    ax.add_patch(plt.Polygon(vertices_left, edgecolor='blue', fill=False))
    drawTriangle(ax, vertices_left, i)


    vertices_right = np.array([[vertices[2][0], vertices[0][1]], [vertices[1][0], vertices[1][1]], [(vertices[1][0] + vertices[2][0]) * 0.5, vertices[2][1] / 2]])
    print(vertices_right)
    ax.add_patch(plt.Polygon(vertices_right, edgecolor='blue', fill=False))
    drawTriangle(ax, vertices_right, i)
    
    # vertices_up = np.array([[0.5 / 2, calcHeight(0.5)], [(0.5 + 1) / 2, calcHeight(0.5)], [1 / 2, calcHeight(1)]])
    # ax.add_patch(plt.Polygon(vertices_up, edgecolor='blue', fill=False))


vertices = np.array([[0, 0], [1, 0], [0.5, calcHeight(1)]])

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, calcHeight(1))
ax.set_aspect('equal')



triangle_outline = plt.Polygon(vertices, edgecolor='red', fill=False)
ax.add_patch(triangle_outline)
drawTriangle(ax, [[0, 0], [1, 0], [0.5, calcHeight(1)]], 0)

plt.show()
