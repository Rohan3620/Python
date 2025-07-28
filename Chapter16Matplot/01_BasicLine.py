import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(0,10,20)
plt.figure(figsize=(6,6))
ax1=plt.subplot()
ax1.plot(a,linewidth=1,linestyle="-",color="r",marker='o',alpha=0.5)
plt.xlabel("No of Point",fontsize=25,fontweight="bold")
plt.ylabel("No of values",fontsize=25,fontweight="bold")
plt.title("Line plot")
plt.grid=True
plt.show()

""" 
o-circle marker
^-trinagle marker
+-plus marker 
D-Diamond marker 
s-Square marker

color 
r- red
g-green
b-blue
c-cyan
m-mangenta
"""