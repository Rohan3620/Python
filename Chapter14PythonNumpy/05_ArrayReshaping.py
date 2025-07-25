
import numpy as np
# Reshaping 
a = np.arange(24, dtype = float)
print(a)
print(np.ndim(a))
print()
b = a.reshape(6,4)
print("Reshaped to 6x4:\n",b)
print(np.ndim(b))
print()
c = a.reshape(2,3,4)
print(c)
print(np.ndim(c))







