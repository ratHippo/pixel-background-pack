import colors,random
from PIL import Image, ImageOps
width = 48
height = 30
palette = ["c98686","81a79d","8ac1e2","8fd6f5","dce0e4"] #Sea Wolf Rev 2, example pallete
img  = Image.new( mode = "RGB", size = (width, height) )
pixels = img.load()
for i in range(width):
    for j in range(height):
        color = tuple(colors.hex(random.choice(palette)).rgb)
        pixels[i,j] = color
img = img.resize((2560,1600),0)
img.show()
