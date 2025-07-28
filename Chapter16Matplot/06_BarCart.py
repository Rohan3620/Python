import matplotlib.pyplot as plt
import numpy as np
x=['A','B','C','D','E']
y=[10,20,30,25,15]

plt.figure(figsize=(5,2))
ax1=plt.subplot()
ax1.barh(x,y,color=['r','g','k','b','c'])
plt.show()
