import numpy as np

# --------------------------------------------------
# 🔹 1D ARRAY - INDEXING & SLICING
# --------------------------------------------------

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("🔹 1D Array:", arr)

# Basic Indexing
print("First element:", arr[0])       # 10
print("Last element:", arr[-1])       # 100

# Slicing: [start : end] (end not included)
print("Slice [1:4]:", arr[1:4])       # [20 30 40]

# Slicing with step
print("Slice [1:4:2]:", arr[1:4:2])   # [20 40]

# --------------------------------------------------
# 🔹 BOOLEAN INDEXING
# --------------------------------------------------

data = np.array([1, 2, 3, 4, 5])
print("\n🔹 Boolean Indexing Example:")
print("Original:", data)
print("Values > 3:", data[data > 3])  # [4 5]

# --------------------------------------------------
# 🔹 2D ARRAY - INDEXING & SLICING
# --------------------------------------------------

a = np.array([
    [10, 20, 30, 40],
    [11, 21, 31, 41]
])

print("\n🔹 2D Array:\n", a)

# Indexing a single element
print("Element at [0, 3]:", a[0, 3])   # 40

# Slicing rows and columns: a[row_start:row_end, col_start:col_end]
print("Slice [0:1, 1:3]:\n", a[0:1, 1:3])  # [[20 30]]
print("Slice [0:2, 1:3]:\n", a[0:2, 1:3])  # [[20 30], [21 31]]

# --------------------------------------------------
# 🔹 ADVANCED 2D SLICING
# --------------------------------------------------

a = np.array([
    [10, 20, 30, 40],
    [11, 21, 31, 41],
    [12, 22, 32, 42]
])

print("\n🔹 Advanced 2D Slicing:\n", a)

# Select rows 0 and 2, columns 0 and 3
# Equivalent to: a[0:3:2, 0:4:3]
print("Selected rows 0 & 2, columns 0 & 3:\n", a[0::2, 0::3])
