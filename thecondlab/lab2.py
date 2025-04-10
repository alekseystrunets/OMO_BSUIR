import numpy as np

A=0
C=4
B=1

print('w0 = ', C, '; w1 = ', A, '; w2 = ', B)

w = np.array([A,B])
x = np.array([[2, 3], [5, 7], [6, 5], [7, 2]])
y = np.array([1, 1, -1, -1])

margin = []

for i, row in enumerate(x):
    summa = y[i] * (np.dot(w, row) - C)
    margin.append(int(summa))

print("margin = ", margin)