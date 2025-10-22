import matplotlib.pyplot as plt
import numpy as np

x=range(5)
y=[[1,2,3,4,5],
  [5,2,1,3,1]]

plt.figure(figsize=(5,2))
ax1=plt.subplot()
ax1.stackplot(x,y)
plt.grid=True
plt.show()
