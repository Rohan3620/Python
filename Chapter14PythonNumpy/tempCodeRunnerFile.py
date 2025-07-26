import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Image A
path = r"C:\Users\C9IN\Downloads\Data\A.jpg"
img = Image.open(path)
img_arr = np.array(img)

img_arr[0:3000, 0:2000, 1] = 0
img_arr[0:3000, 2000:, 0] = 255
img_arr[3000:, 0:2000, 2] = 0
img_arr[3000:, 2000:, [2, 1]] = 2

plt.imshow(img_arr)
plt.show()