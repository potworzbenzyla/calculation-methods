import numpy as np

A = np.array([[10.0, 40.0, 70.0], [20.0, 50.0, 80.0], [30.0, 60.0, 80.0]])
B = np.array([[300.0], [360.0], [390.0]])
x = np.array([[0.0], [0.0], [0.0]])

detA = np.linalg.det(A)

if detA == 0:
    print("nie ma rozwiazan")
else:
    for k in range(0,B.shape[0]):
        M = A.copy()
        M[:,k] = B.squeeze().copy()
        x[k] = np.linalg.det(M)/detA

print(x)
