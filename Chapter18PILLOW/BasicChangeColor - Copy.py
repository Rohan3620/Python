#seaborn ka dataset par  countplot , boxplot ,scatter plot ,heatmap
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
path = r"C:\Users\C9IN\Downloads\Data\E.jpg"
img = Image.open(path)
plt.imshow(img)
plt.show()
resized = img.resize((200, 200))
gray = img.convert("L")
gray.save("gray_sample.jpg")
img = Image.open("gray_sample.jpg")
plt.imshow(img)
plt.show()