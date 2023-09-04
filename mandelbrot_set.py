import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2.0, 1)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def modifyColorMapping(n, max_iters):
    color = np.log(n + 1) / np.log(max_iters)
    return color

def isInMandelbrotSet(c, maxIters):
    z = np.zeros_like(c)
    n = np.zeros(c.shape, dtype=int)

    
    for i in range(maxIters):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] * z[mask] + c[mask]
        n[mask] += 1

    return n


if __name__ == "__main__":
    width, height = 800, 800  # Image resolution
    x_min, x_max = -2.0, 1.0    # X-axis range
    y_min, y_max = -1.5, 1.5    # Y-axis range
    max_iters = 1000  # Maximum number of iterations

    mandelbrotSet = np.zeros((height, width))

    real_vals = np.linspace(x_min, x_max, width)
    imag_vals = np.linspace(y_min, y_max, height)

    real, imag = np.meshgrid(real_vals, imag_vals)
    c = real + 1j * imag

    mandelbrotSet = isInMandelbrotSet(c, max_iters)

    colorMap = modifyColorMapping(mandelbrotSet, max_iters)

    initFigure()
    plt.imshow(colorMap, extent=(x_min, x_max, y_min, y_max), cmap='inferno')
    plt.show()
