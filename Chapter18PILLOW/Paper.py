from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
img = Image.new("RGB", (200, 100), color="Red")
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Name Rohan\n", fill="black")
draw.text((10, 20), "Course BCA\n", fill="Pink")
draw.text((10, 30), "Section E1\n", fill="white")
draw.text((10, 40), "Rollno 50\n", fill="yellow")

img.save("text_image.png")
img = Image.open("text_image.png")
plt.imshow(img)
plt.show()