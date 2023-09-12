import matplotlib.pyplot as plt
import numpy as np

def tangent_circles(x0, y0, r):
  """Calculates the three tangent circles to a circle centered at (x0, y0) with radius r.

  Args:
    x0: The x-coordinate of the center of the original circle.
    y0: The y-coordinate of the center of the original circle.
    r: The radius of the original circle.

  Returns:
    A list of three tuples, each of which is the center and radius of a tangent circle.
  """

  x1, y1 = x0 + r, y0
  x2, y2 = x0, y0 + r
  x3, y3 = x0 - r, y0

  circles = []
  circles.append((x1, y1, r - 0.5))
  circles.append((x2, y2, r - 0.5))
  circles.append((x3, y3, r - 0.5))

  return circles

def main():
  """Calculates and displays three tangent circles."""

  x0, y0, r = 0, 0, 2

  circles = tangent_circles(x0, y0, r)

  fig, ax = plt.subplots()

  for x, y, r in circles:
    ax.add_artist(plt.Circle((x, y), r, color='r'))

  ax.set_xlim(-3, 3)
  ax.set_ylim(-3, 3)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_title('Three Tangent Circles')

  plt.show()

if __name__ == '__main__':
  main()
