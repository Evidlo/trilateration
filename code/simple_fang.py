from matplotlib import pyplot as plt
import numpy as np

# generate random x
x = np.array([.5, .6])
noise = np.random.normal(0, 0, size=2)

sensors = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    # [1, 1]
])


# distance_diffs = np.linalg.norm(x + noise - sensors[1:], axis=1) - np.linalg.norm(x)
rac = np.linalg.norm(x - sensors[0]) - np.linalg.norm(x)
rab = np.linalg.norm(x - sensors[1]) - np.linalg.norm(x)

c_x = 0
c_y = 1
c = np.linalg.norm((c_x, c_y))
b = 1
g = (rac * (b / rab) - c_x) / c_y
h = (c**2 - rac**2 + rac * rab * (1 - (b / rab)**2)) / (2 * c_y)
d = -(1 - (b / rab)**2 + g**2)
e = b * (1 - (b / rab)**2) - 2 * g * h
f = (rab**2 / 4) * (1 - (b / rab**2))**2 - h**2
# distance_diffs[0] = 0

# phi = np.concatenate((distance_diffs[:, np.newaxis], sensors[1:]), axis=1)
# b = (np.linalg.norm(sensors[1:], axis=1)**2 - distance_diffs**2) / 2

# # compute least squares solution
# x_hat = np.linalg.inv(phi.T @ phi) @ phi.T @ b

# plt.plot(sensors[:, 0], sensors[:, 1], 'k*')
# plt.plot(x[0], x[1], 'ro')
# plt.plot(x_hat[1], x_hat[2], 'bo')
# plt.legend(('Sensors', 'Position', 'Estimate'))
# plt.grid(True)
# plt.show()

x1 = (-e - np.sqrt(e**2 - 4 * d * f)) / (2 * d)
y = np.sqrt((rab**2 - b**2 + 2 * b * x1)**2 / (4 * rab**2) - x1**2)
# y12 = -y11
x2 = (-e + np.sqrt(e**2 - 4 * d * f)) / (2 * d)
# y21 = np.sqrt((rab**2 - b**2 + 2 * b * x2)**2 / (4 * rab**2) - x2**2)
# y22 = -y21
