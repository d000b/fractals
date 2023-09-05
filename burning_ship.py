import numpy as np
import matplotlib.pyplot as plt


def initFigure():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')
    ax.set_aspect('equal')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    return ax, fig

def modifyColorMapping(n, max_iters):
    color = np.log(n + 1) / np.log(max_iters)
    return color

def isInBurningShipSet(c, maxIters):
    z = np.zeros_like(c)
    n = np.zeros(c.shape, dtype=int)

    for i in range(maxIters):
        mask = np.abs(z) <= 2
        z[mask] = (np.abs(np.real(z[mask])) + 1j * np.abs(np.imag(z[mask]))) ** 2 + c[mask]
        n[mask] += 1

    return n


if __name__ == "__main__":
    width, height = 800, 800
    x_min, x_max = -1.83, -1.66
    y_min, y_max = -0.09, 0
    max_iters = 10000

    burningShipSet = np.zeros((height, width))

    real_vals = np.linspace(x_max, x_min, width)
    imag_vals = np.linspace(y_min, y_max, height)

    real, imag = np.meshgrid(real_vals, imag_vals)
    c = real + 1j * imag

    burningShipSet = isInBurningShipSet(c, max_iters)

    colorMap = modifyColorMapping(burningShipSet, max_iters)

    initFigure()
    plt.imshow(colorMap, extent=(x_min, x_max, y_min, y_max), cmap='gray')
    plt.show()
