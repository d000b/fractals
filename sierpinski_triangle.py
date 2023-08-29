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
    
    ax.add_patch(draw_triangle_down(length / 2, [startPos[0], startPos[1]], color))
    # ax.add_patch(draw_triangle_down(length / 2, midpoint(startPos, [length + length / 2, midConstant + midConstant / 2]), 'white'))
    # ax.add_patch(draw_triangle_down(length / 2, midpoint(startPos, [length * 2 + length / 2, midConstant / 2]), 'white'))

    sierpinski_triangle(iterations, length / 2, midpoint([0, 0], [length / 4, startPos[1]]), ax, midConstant, 'white')


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

ax.add_patch(draw_triangle_up(1, [0, 0], 'blue'))
midConstant = 0.8660254
sierpinski_triangle(100, 1, midpoint([0, 0], [0.5, midConstant]), ax, midConstant, 'white')

# # 2nd iter.
# ax.add_patch(draw_triangle_down(0.5 / 2, midpoint([0, 0], [0.5 / 2, 0.8660254 / 2]), 'white'))
# ax.add_patch(draw_triangle_down(0.5 / 2, midpoint([0, 0], [0.5 + 0.5 / 2, 0.8660254 + 0.8660254 / 2]), 'white'))
# ax.add_patch(draw_triangle_down(0.5 / 2, midpoint([0, 0], [0.5 * 2 + 0.25, 0.8660254 / 2]), 'white'))

# ax.add_patch(draw_triangle_down(0.25, midpoint([0, 0], [0.25, 0.8660254 / 2]), 'white'))

plt.show()
