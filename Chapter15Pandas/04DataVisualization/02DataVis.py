import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv(r"C:\Users\C9IN\Downloads\Data\mtcars2.csv")
x=range(32)
y=df['cyl']
plt.plot(x,y)
plt.show()


