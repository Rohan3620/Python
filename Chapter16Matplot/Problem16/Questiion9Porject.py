import matplotlib.pyplot as plt
import numpy as np

x1 = range(6)
y1 = [
    [1, 2, 3, 4, 5, 2],
    [5, 2, 1, 3, 1, 2],
    [1, 2, 3, 4, 5, 2]
]

x2 = ['Google', 'Amazon', 'AWS', 'ISGEC', 'TATA', 'BARCO', 'Abode']
y2 = [100, 250, 350, 250, 150, 300, 200]

x3 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
y3 = [10, 20, 30, 25, 15, 30, 40, 77, 66, 55]
x4 = [10, 20, 30, 40, 50, 0, 90, 20, 30, 40]

x5 = ['Car1', 'Car2', 'Car3', 'Car4', 'Car5']
y5 = [1000000, 2000000, 3000000, 2005000, 1500000]

x6 = [10, 11, 12, 13, 14, 15, 15.5, 16, 16.5, 17, 18, 19, 20, 21.5,
      22, 23.5, 24, 24.5, 25, 26, 27, 28, 29, 30, 31, 32.5, 33,
      34, 35, 36.5, 37, 38, 39, 40]

labels = ['Google', 'Amazon']
sizes = [100, 250]
explode = [0, 0]

x7 = [10, 13, 15, 16, 18, 19, 30, -35, 37, -40, 100, 200]

plt.figure(figsize=(10, 10))
ax1 = plt.subplot(3, 3, 1)
plt.title("Stack Plot")
plt.xlabel("x")
plt.ylabel("Y")
ax2 = plt.subplot(3, 3,2)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
ax3 = plt.subplot(3, 3, 3)
plt.title("Bar Charplt")
plt.xlabel("Company")
plt.ylabel("Value")
ax4 = plt.subplot(3, 3, 4)
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel("Value")
ax5 = plt.subplot(3, 3, 5)
plt.title("Horizontal Bar")
plt.xlabel("Price")
plt.ylabel("car")
ax6 = plt.subplot(3, 3, 6)  
plt.title("Pie Chart")         
ax7 = plt.subplot(3,3,7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Count")
ax8 = plt.subplot(3, 3, 8)
plt.title("Violin Plot")
plt.xlabel("Data")
plt.ylabel("Valuax8")
ax9 = plt.subplot(3, 3, 9)
plt.title("Box Plot")
plt.xlabel("Data")
plt.ylabel("Value")
ax1.stackplot(x1, y1)
plt.sca(ax2)
ax2.bar(x2, y2, color=['r', 'g', 'b', 'orange', 'purple', 'cyan', 'pink'])
ax3.scatter(x3, y3, s=200, marker='d', color='r', edgecolors='g', alpha=0.5)
ax4.plot(x4)
ax5.barh(x5, y5, color=['r', 'g', 'k', 'b', 'c'])
ax6.pie(sizes, explode=explode, labels=labels)
ax7.hist(x6, bins=25, color='r')
ax8.boxplot(x7)
ax9.violinplot(x7)




plt.show()
