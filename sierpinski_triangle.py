# https://mathigon.org/course/fractals/mandelbrot
import matplotlib.pyplot as plt
import numpy as np
import math

def draw_triangle_up(length, startPos, color):
    vertices = np.array([startPos, [startPos[0] + length, startPos[1]], [startPos[0] + length / 2, startPos[1] + length * np.sqrt(3) / 2]])
    return plt.Polygon(vertices, closed=True, fill=True, color=color)

def draw_triangle_down(length, startPos, color):
    vertices = np.array([startPos, [startPos[0] + length, startPos[1]], [startPos[0] + length / 2, startPos[1] - length * np.sqrt(3) / 2]])
    return plt.Polygon(vertices, closed=True, fill=True, color=color)

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def calcHeight(length):
    return math.sin(math.radians(60)) * length

def sierpinski_triangle(iterations, length, startPos, ax, color):
    if iterations <= 0:
        return
    iterations = iterations - 1

    ax.add_patch(draw_triangle_down(length, startPos, color))
    # ax.add_patch(draw_triangle_down(length / 2, midpoint([startPos[0], startPos[1]], [startPos[0] + length / 2, startPos[1] + calcHeight(length)]), 'white'))
    # ax.add_patch(draw_triangle_down(length / 2, midpoint([length * 2, 0], [startPos[0], startPos[1]]), 'white'))

    sierpinski_triangle(iterations, length / 2, midpoint([0, 0], [startPos[0], startPos[1]]), ax, color)
    sierpinski_triangle(iterations, length / 2, midpoint([startPos[0], startPos[1]], [startPos[0] + length / 2, startPos[1] + calcHeight(length)]), ax, 'white')


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')


ax.add_patch(draw_triangle_up(1, [0, 0], 'blue'))
length = 0.5
first_c = midpoint([0, 0], [length, calcHeight(1)])
ax.add_patch(draw_triangle_down(length, first_c, 'white'))
length = length / 2
sierpinski_triangle(4, length, midpoint([0, 0], [length, calcHeight(1) / 2]), ax, 'yellow')
sierpinski_triangle(4, length, midpoint([length, 0], [length * 4, calcHeight(1) / 2]), ax, 'yellow')
sierpinski_triangle(4, length, midpoint([first_c[0], first_c[1]], [first_c[0] + length, first_c[1] + calcHeight(length * 2)]), ax, 'yellow')


plt.show()
