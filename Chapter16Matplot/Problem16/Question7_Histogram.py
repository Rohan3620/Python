import matplotlib.pyplot as plt
import numpy as np

# Manually entered, more "continuous" looking data
x = [10, 11, 12, 13, 14, 15, 15.5, 16, 16.5, 17, 18, 19, 20, 21.5,
     22, 23.5, 24, 24.5, 25, 26, 27, 28, 29, 30, 31, 32.5, 33,
     34, 35, 36.5, 37, 38, 39, 40]

plt.figure(figsize=(5, 2))
ax1 = plt.subplot(1, 1, 1)
ax1.hist(x, bins=25, color='r')
plt.show()
