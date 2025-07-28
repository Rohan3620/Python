import matplotlib.pyplot as plt
import numpy as np

labels = ['Google', 'Amazon', 'AWS', 'ISGEC', 'TATA']
sizes = [100, 250, 350, 250, 150]
explode = [0, 0, 0.4, 0, 0]  # Length must match 'sizes'

plt.figure(figsize=(5, 2))
ax1 = plt.subplot()
ax1.pie(sizes, explode=explode, labels=labels)
plt.show()
