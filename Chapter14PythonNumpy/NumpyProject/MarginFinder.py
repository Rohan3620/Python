import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
path = r"C:\Users\C9IN\Downloads\Data\E.jpg"
img = Image.open(path)
img_arr = np.array(img)
points = []
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        points.append((x, y))
        print(f"Point {len(points)}: (x={x}, y={y})")
        # Draw red dot
        plt.plot(x, y, 'ro')
        plt.draw()
fig, ax = plt.subplots()
ax.imshow(img_arr)
plt.title("Click TOP-LEFT and BOTTOM-RIGHT corners of the FACE region")
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

if len(points) == 2:
    (x1, y1), (x2, y2) = points
    y1, y2 = sorted([y1, y2])
    x1, x2 = sorted([x1, x2])

    
    plt.imshow(img_arr)
    plt.show()
else:
    print("You need to click exactly TWO points!")
