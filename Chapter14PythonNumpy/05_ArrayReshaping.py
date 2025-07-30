import numpy as np

# 🔹 Create a 1D array of 24 float values
a = np.arange(24, dtype=float)
print("Original 1D array:")
print(a)
print("Number of dimensions:", np.ndim(a))
print()

# 🔹 Reshape the 1D array to a 2D array (6 rows, 4 columns)
b = a.reshape(6, 4)
print("Reshaped to 2D (6x4):")
print(b)
print("Number of dimensions:", np.ndim(b))
print()

# 🔹 Reshape the same array to a 3D array (2 blocks, 3 rows, 4 columns)
c = a.reshape(2, 3, 4)
print("Reshaped to 3D (2x3x4):")
print(c)
print("Number of dimensions:", np.ndim(c))
print()

# 🔄 Transpose the 3D array (default axis change: (0, 1, 2) → (2, 1, 0))
print("Transposed 3D array (shape changes to 4x3x2):")
print(c.transpose())
for i in a.flat:
    print(i,end=" ")