import numpy as np

A = np.array([[2.0, 1.0, 4.0], [4.0, 3.0, 6.0], [3.0, 6.0, 8.0]])
b = np.array([[11.0], [23.0], [32.0]])
x = np.array([[0.0], [0.0], [0.0]])
n = b.shape[0]

for k in range (0, n-1):
    for i in range(k+1, n):
        L = A[i,k]/A[k,k]
        for j in range(k+1,n):
            A[i, j ] = A[i, j] - L * A[k,j]
        b[i] = b[i]-L*b[k]

x = b.copy() 

for i in range(n-1, -1, -1):
    s=0.0
    for j in range(i+1,n):
        s=s+A[i,j]*x[j]
    x[i]=(x[i]-s)/A[i,i]
print(x)