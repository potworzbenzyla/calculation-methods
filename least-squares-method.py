import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as slm

X = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]]) 
Y = np.array([0.1, 7.7, 13.6, 27.2, 40.9, 61.1])


regresja = slm.LinearRegression()

regresja.fit(X,Y)

#P = np.array([0.098*x + 0.006 for x in np.linspace(1,11,50)])

plt.figure()
plt.scatter(X, Y, c='r', s=1.5)
#plt.plot(np.linspace(1,11,50), P)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Zebrane dane')
plt.show()