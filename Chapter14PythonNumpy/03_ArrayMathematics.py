import numpy as np

# Creating two 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise operations
print("\nAddition:", x + y)                 # [5 7 9]
print("Subtraction:", x-y)
print("Multiplication:", x * y)             # [4 10 18]
print("Square of x:", x**2)                 # [1 4 9]

# Sum of all elements from both arrays
print("Total Sum (x and y):", np.sum([x, y]))  # 21

# Element-wise subtraction and division
print("Subtraction:", np.subtract(x, y))       # [-3 -3 -3]
print("Multiplication:", np.multiply(x, y))    # [4 10 18]
print("Division:", np.divide(x, y))            # [0.25 0.4 0.5]

# Statistical functions
print("Mean of x:", np.mean(x))                # 2.0
print("Max of y:", np.max(y))                  # 6
print("Min of y:", np.min(y))                  # 4
print("Median of y:", np.median(y))            # 5.0
print(np.std(x))
print(np.argmin(x))
print(np.sqrt(x))
print(np.sin(x))
print(np.cos(x))
print(np.cumsum(x))


print("\nBroadcasting Example:")
arr = np.array([1, 2, 3])
print("Add 10 to every element:", arr + 10)