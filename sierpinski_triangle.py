# https://mathigon.org/course/fractals/mandelbrot
import matplotlib.pyplot as plt
import numpy as np

def draw_triangle_up(length, startPos, color):
    vertices = np.array([startPos, [startPos[0] + length, startPos[1]], [startPos[0] + length / 2, startPos[1] + length * np.sqrt(3) / 2]])
    return plt.Polygon(vertices, closed=True, fill=True, color=color)

def draw_triangle_down(length, startPos, color):
    vertices = np.array([startPos, [startPos[0] + length, startPos[1]], [startPos[0] + length / 2, startPos[1] - length * np.sqrt(3) / 2]])
    return plt.Polygon(vertices, closed=True, fill=True, color=color)

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


def sierpinski_triangle(iterations, length, startPos, ax, midConstant, color):
    if iterations <= 0:
        return
    iterations = iterations - 1

    # ax.plot(startPos[0], startPos[1], marker='o', color='green', markersize=8)
    ax.plot(startPos[0] + midConstant / 4, startPos[1] + midConstant / 2, marker='o', color='purple', markersize=8)

    ax.add_patch(draw_triangle_down(length / 2, midpoint([0, 0], [startPos[0], startPos[1]]), color))
    ax.add_patch(draw_triangle_down(length / 2, midpoint([startPos[0], startPos[1]], [startPos[0] + length, startPos[1] + length]), "pink"))
    
    # ax.add_patch(draw_triangle_down(length / 2, [startPos[0], startPos[1]], color))
    # ax.add_patch(draw_triangle_down(length / 2, [startPos[0] + length * 2, startPos[1]], "green"))

    # ax.add_patch(draw_triangle_down(length / 2, midpoint(startPos, [length + length / 2, midConstant + midConstant / 2]), 'white'))
    # ax.add_patch(draw_triangle_down(length / 2, midpoint(startPos, [length * 2 + length / 2, midConstant / 2]), 'white'))

    sierpinski_triangle(iterations, length / 2, midpoint([0, 0], [startPos[0], startPos[1]]), ax, midConstant, 'yellow')
    # sierpinski_triangle(iterations, length / 2, midpoint([startPos[0], startPos[1]], [length / 4, startPos[1]]), ax, midConstant, 'yellow')


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

midConstant = 0.8660254
ax.add_patch(draw_triangle_up(1, [0, 0], 'blue'))
first_c = midpoint([0, 0], [0.5, midConstant])

ax.add_patch(draw_triangle_down(0.5, first_c, 'white'))

sierpinski_triangle(4, 0.5, first_c, ax, midConstant, 'yellow')


plt.show()
