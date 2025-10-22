import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(0,10,20)
b=np.linspace(2,10,20)
c=np.linspace(1,10,20)
plt.figure(figsize=(2,2))
ax1=plt.subplot()
ax2=plt.subplot()
ax3=plt.subplot()
ax1.plot(a)
ax2.plot(b)
ax3.plot(c)
plt.grid=True
plt.show()
