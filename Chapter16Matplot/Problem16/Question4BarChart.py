import matplotlib.pyplot as plt
import numpy as np
x=['Apple','Banana','Fig','Mango','Grapes']
y=[100,200,300,250,150]

plt.figure(figsize=(5,2))
ax1=plt.subplot()
ax1.barh(x,y,color=['r','g','k','b','c'])
plt.title("Fruit price")
plt.xlabel("Fruit")
plt.ylabel("Price")
plt.show()
