import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv(r"C:\Users\C9IN\Desktop\coding\Python\Chapter15Pandas\Data\mtcars2.csv")
x=range(32)
y=df['hp']
plt.bar(x,y)
plt.show()


