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

# Image B
path = r"C:\Users\C9IN\Downloads\Data\B.jpg"
img = Image.open(path)
img_arr = np.array(img)

img_arr[0:1800, 0:1500, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr[0:1800, 1500:, 0] = 3
plt.imshow(img_arr)
plt.show()

img_arr[1800:, 0:1500, 2] = 0
plt.imshow(img_arr)
plt.show()

img_arr[0:, 1500:, [1, 2]] = 9
plt.imshow(img_arr)
plt.show()

# Image C
path = r"C:\Users\C9IN\Downloads\Data\c.jpg"
img = Image.open(path)
img_arr = np.array(img)

img_arr[0:2000, 0:1500, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr[0:2000, 1500:, 0] = 3
plt.imshow(img_arr)
plt.show()

img_arr[2000:, 0:1500, 2] = 0
plt.imshow(img_arr)
plt.show()

img_arr[0:, 1500:, [1, 0]] = 1
plt.imshow(img_arr)
plt.show()

# Image D
path = r"C:\Users\C9IN\Downloads\Data\D.jpg"
img = Image.open(path)
img_arr = np.array(img)

img_arr[0:3500, 0:2200, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr[0:3500, 2200:, 0] = 2
plt.imshow(img_arr)
plt.show()

img_arr[3500:, 0:2200, 2] = 1
plt.imshow(img_arr)
plt.show()

img_arr[0:, 2200:, [2, 0]] = 1
plt.imshow(img_arr)
plt.show()
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ========== IMAGE A ==========
path = r"C:\Users\C9IN\Downloads\Data\A.jpg"
img = Image.open(path)
original_arr = np.array(img)

img_arr = original_arr.copy()
img_arr[0:3000, 0:2000, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[0:3000, 2000:, 0] = 255
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[3000:, 0:2000, 2] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[3000:, 2000:, [2, 1]] = 2
plt.imshow(img_arr)
plt.show()

# ========== IMAGE B ==========
path = r"C:\Users\C9IN\Downloads\Data\B.jpg"
img = Image.open(path)
original_arr = np.array(img)

img_arr = original_arr.copy()
img_arr[0:1800, 0:1500, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[0:1800, 1500:, 0] = 3
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[1800:, 0:1500, 2] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[1800:, 1500:, [1, 2]] = 9
plt.imshow(img_arr)
plt.show()

# ========== IMAGE C ==========
path = r"C:\Users\C9IN\Downloads\Data\c.jpg"
img = Image.open(path)
original_arr = np.array(img)

img_arr = original_arr.copy()
img_arr[0:2000, 0:1500, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[0:2000, 1500:, 0] = 3
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[2000:, 0:1500, 2] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[2000:, 1500:, [1, 0]] = 1
plt.imshow(img_arr)
plt.show()

# ========== IMAGE D ==========
path = r"C:\Users\C9IN\Downloads\Data\D.jpg"
img = Image.open(path)
original_arr = np.array(img)

img_arr = original_arr.copy()
img_arr[0:3500, 0:2200, 1] = 0
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[0:3500, 2200:, 0] = 2
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[3500:, 0:2200, 2] = 1
plt.imshow(img_arr)
plt.show()

img_arr = original_arr.copy()
img_arr[3500:, 2200:, [2, 0]] = 1
plt.imshow(img_arr)
plt.show()
