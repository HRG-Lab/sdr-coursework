#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
sin = np.sin(t)
cos = np.cos(t)

plt.rcParams.update({'font.size': 18})

plt.plot(t, sin, 'r')
plt.plot(t, cos, 'b')

plt.xlabel("Amplitude")
plt.ylabel("Time")

plt.show()
