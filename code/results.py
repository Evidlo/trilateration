from matplotlib import pyplot as plt
import numpy as np


sensors = np.array([
    [0, 0],
    [0.5, .5 * np.sqrt(3)],
    [-0.5, .5 * np.sqrt(3)],
])

# actual
xs = np.array([
    [-1, 1.5],
    [1, 1.5],
    [-1, -1],
    [2, -2],
])


# measured and computed
x_hats = np.array([
    [-1.23, 1.44],
    [1.12, 1.54],
    [-1.42, -1.34],
    [2.21, -2.14],
])

plt.plot(sensors[:, 0], sensors[:, 1], 'k*')
plt.plot(xs[:, 0], xs[:, 1], 'ro', zorder=10)

plt.plot(x_hats[:, 0], x_hats[:, 1], 'bo')

plt.legend(('Sensors', 'Position', 'Estimate'))
plt.grid(True)
plt.show()
