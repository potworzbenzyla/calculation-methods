import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from scipy.interpolate import lagrange

x = np.array([1.0, 2.0, 2.5, 3.0, 4.0, 5.0])
y = np.array([0.0, 5.0, 6.5, 7.0, 3.0, 1.0])
n = 2
p = np.zeros([n, n+1])
value = 3.4

for i in range(n):
    p[i, 0] = x[i]
    p[i, 1] = y[i]

for i in range(2, n+1):
    for j in range(n+1-i):
        p[j, i] = (p[j+1, i-1]-p[j, i-1])/(x[j+i-1]-x[j])

np.set_printoptions(suppress=True)

b = p[0][1:]
print("Pierwsze i drugie wywolanie = ", b)

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
