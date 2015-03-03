# ascii-factory
# Kinman Covey
# 3/2/2015

from PIL import Image
import sys

#filename = raw_input("Enter filename (or path from current directory): ")
filename = "KINMAN COVEY.jpg"
image = Image.open(filename)
print "Image size: " + str(image.size)

w, h = image.size
lim_w = w / h
lim_h = h / w
obj = image.load()

for i in range(0, h):
    for j in range(0, w):
        if i % 5 == 0 and j % 2 == 0:
            r, g, b = obj[j,i]
            if r <= 25 and g <= 25 and b <= 25:
                sys.stdout.write("#")
            elif r <= 50 and g <= 50 and b <= 50:
                sys.stdout.write("%")
            elif r <= 75 and g <= 75 and b <= 75:
                sys.stdout.write("I")
            elif r <= 100 and g <= 100 and b <= 100:
                sys.stdout.write(":")
            elif r <= 125 and g <= 125 and b <= 125:
                sys.stdout.write("+")
            elif r <= 150 and g <= 150 and b <= 150:
                sys.stdout.write("-")
            elif r <= 175 and g <= 175 and b <= 175:
                sys.stdout.write(".")
            else:
                sys.stdout.write(".")             
    if i % 5 == 0:
        print
