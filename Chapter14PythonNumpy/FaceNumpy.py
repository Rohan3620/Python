import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# Load the image
path = r"C:\Users\C9IN\Downloads\Data\E.jpg"
img = Image.open(path)
img_arr = np.array(img)

# 💗 17-point polygon for face
points1 = np.array([
    [1662, 1650],
    [2391, 1615],
    [2392, 782],
    [2279, 733],
    [2189, 740],
    [2092, 774],
    [2002, 740],
    [1925, 740],
    [1828, 795],
    [1758, 865],
    [1738, 948],
    [1724, 1080],
    [1710, 1163],
    [1703, 1247],
    [1696, 1365],
    [1696, 1441],
    [1696, 1532]
], dtype=np.int32)

# 💙 24-point polygon for side
points2 = np.array([
    [3078, 1662],
    [2391, 1615],
    [2356, 767],
    [2349, 747],
    [2418, 747],
    [2432, 733],
    [2488, 747],
    [2564, 767],
    [2613, 781],
    [2655, 733],
    [2752, 733],
    [2814, 726],
    [2905, 774],
    [2953, 858],
    [2988, 941],
    [2995, 1031],
    [3009, 1108],
    [3030, 1212],
    [3030, 1302],
    [3023, 1379],
    [3044, 1455],
    [3072, 1539],
    [3078, 1636],
    [3092, 1692]
], dtype=np.int32)

# 🧡 14-point polygon for lower margin
points3 = np.array([
    [1662, 1650],
    [2391, 1615],
    [2356, 2775],
    [2147, 2727],
    [2043, 2636],
    [1946, 2567],
    [1876, 2518],
    [1807, 2379],
    [1744, 2268],
    [1696, 2129],
    [1696, 2004],
    [1661, 1900],
    [1668, 1844],
    [1654, 1789]
], dtype=np.int32)

# 💚 New 17-point region from last input
points4 = np.array([
    [3078, 1662],
    [2391, 1615],
    [2356, 2775],
    [2384, 2743],
    [2460, 2723],
    [2543, 2723],
    [2613, 2695],
    [2675, 2653],
    [2731, 2591],
    [2780, 2556],
    [2856, 2479],
    [2919, 2417],
    [2919, 2361],
    [2960, 2292],
    [2995, 2174],
    [3009, 1942],
    [3037, 1872],
    [3065, 1726]
], dtype=np.int32)

# Create masks
mask1 = np.zeros_like(img_arr)  # Face
mask2 = np.zeros_like(img_arr)  # Side
mask3 = np.zeros_like(img_arr)  # Lower
mask4 = np.zeros_like(img_arr)  # New right region


cv2.fillPoly(mask1, [points1], color=(0, 255, 255))    # 💙 Top-Left (Cyan)
cv2.fillPoly(mask2, [points2], color=(255, 0, 0))      # ❤️ Top-Right (Red)e
cv2.fillPoly(mask3, [points3], color=(255, 0, 255))    # 💗 Bottom-Left (Magenta/Pink)w/Cyan-ish
cv2.fillPoly(mask4, [points4], color=(0, 255, 0))      # 💚 Bottom-Right (Green)

# Apply in proper layering order
img_arr[np.where(mask1 != 0)] = mask1[np.where(mask1 != 0)]
img_arr[np.where(mask3 != 0)] = mask3[np.where(mask3 != 0)]
img_arr[np.where(mask2 != 0)] = mask2[np.where(mask2 != 0)]
img_arr[np.where(mask4 != 0)] = mask4[np.where(mask4 != 0)]

# Show result
plt.imshow(img_arr)


plt.show()
