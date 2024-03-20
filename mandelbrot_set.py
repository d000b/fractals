import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class Context:
    def __init__(self):
        self.axis = None

        self.screenspace = 1000, 1000  # Image resolution
        self.x = -2.0, 1.0  # X-axis range
        self.y = -1.5, 1.5  # Y-axis range
        self.iterations = 100  # Maximum number of iterations


def initFigure(x, y):
    fig, ax = plt.subplots(figsize=(6, 6))

    x_min, x_max = x
    y_min, y_max = y

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

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


def maldebrot_impl(x, y, screenspace, iterations):
    x_min, x_max = x
    y_min, y_max = y
    width, height = screenspace

    re = np.linspace(x_min, x_max, width)
    im = np.linspace(y_min, y_max, height)

    real, imag = np.meshgrid(re, im)
    c = real + 1j * imag

    mandelbrotSet = isInMandelbrotSet(c, iterations)

    return mandelbrotSet


def update(ctx: Context):
    mandelbrotSet = maldebrot_impl(ctx.x, ctx.y, ctx.screenspace, ctx.iterations)

    colorMap = modifyColorMapping(mandelbrotSet, ctx.iterations)

    if ctx.axis is None:
        axis, figure = initFigure(ctx.x, ctx.y)
        ctx.axis = axis

    plt.imshow(colorMap, extent=(*ctx.x, *ctx.y), cmap='inferno')
    plt.show()


class Zoomable:
    def __init__(self, plot, context: Context):
        self.plot = plot
        self.context = context

        self.x = None
        self.y = None

        self.pressing = None
        self.releasing = None
        self.moving = None

        self.connect()

    def connect(self):
        self.pressing = self.plot.connect('button_press_event', self.on_press)
        self.releasing = self.plot.connect('button_release_event', self.on_release)
        self.moving = self.plot.connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        self.x = event.xdata, None
        self.y = event.ydata, None

        print(self.x, self.y)

    def on_motion(self, event):
        pass

    def on_release(self, event):
        x, _ = self.x
        y, _ = self.y

        self.context.x = x, event.xdata
        self.context.y = y, event.ydata

        print(self.context.x, self.context.y)

        update(self.context)

    def disconnect(self):
        self.plot.disconnect(self.pressing)
        self.plot.disconnect(self.releasing)
        self.plot.disconnect(self.moving)


if __name__ == "__main__":
    zoom = Zoomable(plot=plt, context=Context())

    update(zoom.context)

