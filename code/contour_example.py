import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


delta = 0.025
x = np.arange(0, 1.0, delta)
y = np.arange(0, 1.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y)**2)
Z3 = np.exp(-(X)**2 - (Y - 1)**2)
Z4 = np.exp(-(X - 0.5)**2 - (Y - 0.5)**2)
Z = (Z1 + Z2 + Z3 + Z4)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, fontsize=10)
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.show()

from matplotlib import pyplot as plt
import numpy as np

# generate random x
# x = np.random.random(2)
x = np.array([.35, .39])
noise = np.random.normal(0, 0, size=2)

sensors = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

distance_diffs = np.linalg.norm(x + noise - sensors, axis=1) - np.linalg.norm(x)

phi = np.concatenate((distance_diffs[:, np.newaxis], sensors), axis=1)
b = (np.linalg.norm(sensors, axis=1)**2 - distance_diffs**2) / 2

# compute least squares solution
x_hat = np.linalg.inv(phi.T @ phi) @ phi.T @ b


delta = 0.025
x = np.arange(0, 1.0, delta)
y = np.arange(0, 1.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y)**2)
Z3 = np.exp(-(X)**2 - (Y - 1)**2)
Z4 = np.exp(-(X - 0.5)**2 - (Y - 0.5)**2)
Z = (Z1 + Z2 + Z3 + Z4)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)

plt.plot(sensors[:, 0], sensors[:, 1], 'k*')
# plt.plot(x[0], x[1], 'ro')
plt.plot(x_hat[1], x_hat[2], 'bo')
plt.xlim([-.1, 1.1])
plt.ylim([-.1, 1.1])
plt.legend(('Sensors', 'Position'))
plt.show()
