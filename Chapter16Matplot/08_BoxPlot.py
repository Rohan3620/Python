import matplotlib.pyplot as plt
import numpy as np
x=[10,13,15,16,18,19,30,35,37,40]
plt.figure(figsize=(5,2))
ax1=plt.subplot()
ax1.boxplot(x)
plt.show()
