import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
path = r"C:\Users\C9IN\Downloads\Data\A.jpg"
img = Image.open(path)
img_arr = np.array(img)
plt.imshow(img_arr)
