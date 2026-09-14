import numpy as np

# Matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Addition using Python lists
C = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("Addition using Python List:")
print(C)

# Addition using NumPy
A_np = np.array(A)
B_np = np.array(B)

C_np = A_np + B_np

print("Addition using NumPy:")
print(C_np)