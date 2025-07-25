import numpy as np
# Indexing & Slicing
arr = np.array([10, 20, 30, 40, 50,60,70,80,90,100])
print("\nOriginal Array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])
print("Slice [1:4:2]:", arr[1:4:2])


# Reshaping 
reshaped = arr.reshape(5,2 )
print("Reshaped to 5x2:\n", reshaped)

reshaped = arr.reshape(2, 5)
print("Reshaped to 2x5:\n", reshaped)

# Identity Matrix
eye = np.eye(3)
print("Identity Matrix (3x3):\n", eye)

#  Broadcasting Example
print("\nBroadcasting Example:")
arr = np.array([1, 2, 3])
print("Add 10 to every element:", arr + 10)

#  Boolean Indexing
data = np.array([1, 2, 3, 4, 5])
print("Values > 3:", data[data > 3])


