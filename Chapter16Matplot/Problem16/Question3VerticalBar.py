import matplotlib.pyplot as plt
import numpy as np
x=['Google','Amazon','AWS','ISGEC','TATA']
y=[100,250,350,250,150]

plt.figure(figsize=(5,2))
ax1=plt.subplot()
ax1.bar(x,y,color=['r','g'])
import matplotlib.pyplot as plt
import numpy as np

x = ['Google', 'Amazon', 'AWS', 'ISGEC', 'TATA']
y = [100, 250, 350, 250, 150]

plt.figure(figsize=(5, 2))
ax1 = plt.subplot()
ax1.bar(x, y, color=['r', 'g', 'b', 'orange', 'purple'])

plt.title("Company Record")
plt.xlabel("Companies")
plt.ylabel("No of employee")

plt.show()


