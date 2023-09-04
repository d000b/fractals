import numpy as np
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    ax.set_aspect('equal')
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def modifyColorMapping(n, max_iters):
    color = np.log(n + 1) / np.log(max_iters)
    return color

def isInJuliaSet(z, c, maxIters):
    n = np.zeros_like(z, dtype=int)
    for i in range(maxIters):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] * z[mask] + c
        n[mask] += 1
    return n


if __name__ == "__main__":
    width, height = 800, 800  # Image resolution
    x_min, x_max = -1.5, 1.5  # X-axis range
    y_min, y_max = -1.5, 1.5  # Y-axis range
    max_iters = 1000  # Maximum number of iterations

    juliaSet = np.zeros((height, width), dtype=int)

    real_vals = np.linspace(x_min, x_max, width)
    imag_vals = np.linspace(y_min, y_max, height)

    real, imag = np.meshgrid(real_vals, imag_vals)
    z = real + 1j * imag

    # Julia
    c = -0.7 + 0.27015j

    # Siegel disk
    # c = -0.123 + 0.745j

    # Satan
    # c = 0.355 + 0.355j

    # San Marco Fractal
    # c = -0.70176 - 0.3842j

    # Elephant Valley
    # c = 0.275 - 0.007j

    # Neurotic Fish
    # c = 0.6 + 0.6j

    # The Seahorse Valley
    # c = 0.38 + 0.6j
    
    # c = 0 + 1j
    # c = -0.638172 + 0.231726318j

    juliaSet = isInJuliaSet(z, c, max_iters)

    colorMap = modifyColorMapping(juliaSet, max_iters)

    ax, fig = initFigure()
    plt.imshow(colorMap, extent=(x_min, x_max, y_min, y_max), cmap='inferno')
    plt.show()
