from matplotlib import pyplot as plt
import numpy as np


sensors = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# generate random x
# xs = np.random.random((1, 2))
xs = np.array([
    [.25, .25],
    [.25, .75],
    [.75, .25],
    [.75, .75],
    [.7, 1.5],
    [2, 2],
    [1.5, .25],
])

for x in xs:
    plt.plot(sensors[:, 0], sensors[:, 1], 'k*')
    plt.plot(x[0], x[1], 'ro', zorder=10)

    for _ in range(20):
        noise = np.random.normal(0, 0.01, size=2)
        distance_diffs = np.linalg.norm(x + noise - sensors, axis=1) - np.linalg.norm(x)
        # distance_diffs[0] = 0

        phi = np.concatenate((distance_diffs[:, np.newaxis], sensors), axis=1)
        b = (np.linalg.norm(sensors, axis=1)**2 - distance_diffs**2) / 2

        # compute least squares solution
        x_hat = np.linalg.inv(phi.T @ phi) @ phi.T @ b

        plt.plot(x_hat[1], x_hat[2], 'bo')

plt.legend(('Sensors', 'Position', 'Estimate'))
plt.grid(True)
plt.show()
