from matplotlib import pyplot as plt
from itertools import product
import numpy as np

sensors = np.array([
    [0, 0],
    [0, 1],
    # [1, 0],
    # [1, 1]
])

# generate random x
# xs = np.random.random((1, 2))
xs = np.array([
    [.4, .4],
    [.4, 1],
    [-.25, .4],
])
# xs = np.array([
#     [3, 4],
#     [3, 1.5],
# ])

# plt.plot(sensors[:, 1], sensors[:, 0], 'k*')
plt.plot([-.5, .5], [.5, .5], 'k*')
# for x in xs:
    # plt.plot(x[0], x[1], 'ro', zorder=10)

    # for _ in range(20):
    #     noise = np.random.normal(0, 0.01, size=2)
    #     distance_diffs = np.linalg.norm(x + noise - sensors, axis=1) - np.linalg.norm(x)

    #     phi = np.concatenate((distance_diffs[:, np.newaxis], sensors), axis=1)
    #     b = (np.linalg.norm(sensors, axis=1)**2 - distance_diffs**2) / 2

    #     # compute least squares solution
    #     x_hat = np.linalg.inv(phi.T @ phi) @ phi.T @ b

        # plt.plot(x_hat[1], x_hat[2], 'bo')

# plt.legend(('Sensors', 'Position', 'Estimate'))
plt.grid(True)

contour_sample = 1000
# x = y = np.linspace(-.5, 1.5, 1000)
x  = np.linspace(-.75, .75, 1000)
y = np.linspace(-.5, 1.5, 1000)
# x = y = np.linspace(-.5, 5, 1000)
xx, yy = np.meshgrid(x, y)
plt.contour(xx, yy, np.linalg.norm((0, 1) - np.array(list(product(x, y))).reshape(contour_sample, contour_sample, 2), axis=2) - np.linalg.norm(np.array(list(product(x, y))).reshape(contour_sample, contour_sample, 2), axis=2), 20)
# plt.contour(xx, yy, np.linalg.norm(sensors[2] - np.array(list(product(x, y))).reshape(contour_sample, contour_sample, 2), axis=2) - np.linalg.norm(np.array(list(product(x, y))).reshape(contour_sample, contour_sample, 2), axis=2), 20)
# plt.contour(xx, yy, np.linalg.norm(sensors[3] - np.array(list(product(x, y))).reshape(contour_sample, contour_sample, 2), axis=2) - np.linalg.norm(np.array(list(product(x, y))).reshape(contour_sample, contour_sample, 2), axis=2), 20)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
plt.axes().get_xaxis().set_ticklabels([])
plt.axes().get_yaxis().set_ticklabels([])
plt.grid(True)
plt.show()
