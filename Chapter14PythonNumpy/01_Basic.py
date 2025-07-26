"""
NumPy stands for Numerical Python.

 It is mainly used for:
- Working with arrays (1D, 2D, multi-dimensional)
- Fast mathematical operations
- Data manipulation and data generation

 Some key concepts:
- Arrays: Collection of similar data types (NumPy auto-converts all to same type)
- Slicing & Indexing: Just like lists, but faster and more powerful
- Faster than Python lists
- Often used with datasets (like from kaggle.com)
- Great for Data Science and Machine Learning

  Library roles:
- NumPy        → For arrays and numeric operations
- Pandas       → For tabular data (DataFrame, Series)
- Matplotlib   → 2D Data Visualization
- Seaborn      → Statistical Visualizations
"""

import numpy as np  

# Basic Array Creation
a = np.array([10, 20, 30, 40])
print("Integer Array:", a)

a = np.array([10, 20.4, 30, 40])
print("Float Array (auto typecasting):", a)  # All converted to float

a = np.array([1, 2, 3, 4.5, "Rohan"])
print("Mixed Array (converted to string):", a)   

import timeit
# List Comprehension Timing
list_time = timeit.timeit('[j**4 for j in range(1, 9)]', number=1_000_000)
array_time = timeit.timeit('np.arange(1, 9)**4', setup='import numpy as np', number=1_000_000)
print(f"List Comprehension Time (1M runs): {list_time:.6f} seconds")
print(f"NumPy Array Time        (1M runs): {array_time:.6f} seconds")

# Data Generation
# 1. Zeros array
b1 = np.zeros((3, 4))  # matrix of shape 3x4 filled with 0.0
print("\nZeros Array:\n", b1)
# Ones array
b2 = np.ones((3, 4))  # matrix of shape 3x4 filled with 1.0
print("\nones Array:\n", b2)
b3 = np.ones((3, 4))*2  # matrix of shape 3x4 filled with 1.0
print("\nOnes*n Array:\n", b3)
# 2. Linspace - evenly spaced values between 0 and 10 (4 values)
b = np.linspace(0, 10, 4)
print("Linspace (0 to 10 with 4 points):", b)
# 3. Arange - like range(), but returns a NumPy array
# 0 - start, 10 - end point, 4 step size
# last point is not included
c = np.arange(0, 10, 4)  # last value is excluded
print("Arange (step 4):", c)
# feature	     np.arange()	    np.linspace()
# StepSize	     You specify it	    Automatically calculated
# Num of Points  Not fixed	        Fixed (you choose)
# End Included?	 ❌ No	          ✅ Yes
# Good For	     Discrete steps     Smooth curves, plotting, precision
                #  (e.g., 2, 4, 6)

# 4. Full - array of given shape filled with a constant value
d = np.full((3, 4), 5)
print("Full Array (3x4 filled with 5):\n", d)
d2 = np.full((3, 4), "Rohan")
print("Full Array (3x4 filled with Rohan):\n", d2)

# 5. Random float values between 0 and 1
e = np.random.random(5)
print("Random Float Array (0-1):", e)

# 6. Random integers

f = np.random.randint(0, 10)  
print("Random Integer (0-9):", f)

g = np.random.randint(0, 100, size=(3, 4))  # 3x4 matrix with random ints
print("Random Integer Matrix:\n", g)

h=np.random.random(50)+100
print(h)

i=np.empty(4)
print("Empty array",i)
# Identity Matrix
eye = np.eye(3)
print("Identity Matrix (3x3):\n", eye)

