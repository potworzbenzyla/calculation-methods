import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

T = np.array([250, 300, 400, 500])
G = np.array([0.672, 0.616, 0.525, 0.475])
Tx = np.linspace(250, 500, 25)
order = 1
s = InterpolatedUnivariateSpline(T, G, k=order)
Gx = s(Tx)
plt.figure()
plt.plot(T, G)

for order in range(1, 4):
    s = InterpolatedUnivariateSpline(T, G, k=order)
    y = s(Tx)
    plt.plot(Tx, y)

plt.xlabel("kg/m^3")
plt.ylabel("temperatura")
plt.show()