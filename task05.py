import numpy as np

A = np.array([
    [4, 2],
    [3, 5]
])

B = np.array([
    [1, 6],
    [2, 3]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition")
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print(A + B)

print("\nSubtraction")
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print(A - B)

print("\nElement-wise Multiplication")
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print(A * B)

print("\nMatrix Multiplication")
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print(A @ B)

print("\nTranspose of A")
print("Shape of A:", A.shape)
print("Shape of Transpose:", A.T.shape)
print(A.T)

print("\nDeterminant of A")
print("Shape of A:", A.shape)
print(np.linalg.det(A))

print("\nInverse of A")
print("Shape of A:", A.shape)
print(np.linalg.inv(A))