import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,1,2,3,4,1,2,3,4,5,1,2,3,1,2,3,4,5,1,2,3]
y=[10,20,30,25,15,30,40,77,66,55,10,20,30,25,15,30,40,77,66,55,20,30,40,59,60]

plt.figure(figsize=(5,2))
ax1=plt.subplot()
ax1.scatter(x,y,s=200,marker='^',color='r',edgecolors='g',alpha=0.5)
plt.show()
