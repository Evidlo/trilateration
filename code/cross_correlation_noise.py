#!/bin/env python3
from matplotlib import pyplot as plt
import numpy as np

sample_rate = 3000 # Hz
duration = 1 # s
t = np.linspace(0, duration, duration * sample_rate)
# x = np.zeros(duration * sample_rate)
# x[duration * sample_rate // 2] = 1
offset = duration / 2
x = np.sin(2 * np.pi * 300 * (t - offset)) * np.e**(-(t - offset) / .01) * (t > offset)


# maximums = []
# for _ in range(10000):
#     x_noise1 = x + np.random.normal(0, .8, duration * sample_rate)
#     x_noise2 = x + np.random.normal(0, .8, duration * sample_rate)
#     maximums.append(np.argmax(np.correlate(x_noise1, x_noise2, mode='full')))

# plt.hist(maximums, bins=400)



plt.show()
