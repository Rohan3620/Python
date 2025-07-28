import matplotlib.pyplot as plt
import numpy as np

x=range(6)
y=[[1,2,3,4,5,2],
  [5,2,1,3,1,2],
  [1,2,3,4,5,2],
   [5,2,1,3,1,1],
   [5,2,1,3,1,3]
  ]

plt.figure(figsize=(10,5))
ax1=plt.subplot()
ax1.stackplot(x,y)
plt.grid=True
plt.show()
