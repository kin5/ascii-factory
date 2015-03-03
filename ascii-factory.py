# ascii-factory
# Kinman Covey
# 3/2/2015

from PIL import Image
import sys

# Get a filename, and a scale
# Create the image object and print out its dimensions
filename = raw_input("Enter filename (or path from current directory): ")
image = Image.open(filename)
print "Image size: " + str(image.size)

w, h = image.size
    
obj = image.load()

r_min = 255
g_min = 255
b_min = 255

# Find the minimum r, g, and b value for testing purposes
# Found out picture that were really light were not decipherable
# Added this to detect minimum of each and use that as the floor
for i in range(0, h):
    for j in range(0, w):
        if i % 12 == 0 and j % 6 == 0:
            r, g, b = obj[j,i]
            if r < r_min:
                r_min = r

            if g < g_min:
                g_min = g

            if b < b_min:
                b_min = b

# And here's where the magic happens
for i in range(0, h):
    for j in range(0, w):
        if i % 12 == 0 and j % 6 == 0:
            r, g, b = obj[j,i]
            if r <= r_min + 25 and g <= g_min + 25 and b <= b_min + 25:
                sys.stdout.write("#")
            elif r <= r_min + 50 and g <= g_min + 50 and b <= b_min + 50:
                sys.stdout.write("%")
            elif r <= r_min + 75 and g <= g_min + 75 and b <= b_min + 75:
                sys.stdout.write("I")
            elif r <= r_min + 100 and g <= g_min + 100 and b <= b_min + 100:
                sys.stdout.write("i")
            elif r <= r_min + 125 and g <= g_min + 125 and b <= b_min + 125:
                sys.stdout.write("+")
            elif r <= r_min + 150 and g <= g_min + 150 and b <= b_min + 150:
                sys.stdout.write(":")
            elif r <= r_min + 175 and g <= g_min + 175 and b <= b_min + 175:
                sys.stdout.write("-")
            elif r <= r_min + 200 and g <= g_min + 200 and b <= b_min + 200:
                sys.stdout.write("'")
            elif r <= r_min + 225 and g <= g_min + 225 and b <= b_min + 225:
                sys.stdout.write("`")
            else:
                sys.stdout.write(" ")             
    if i % 12 == 0:
        print

# We're done here
print "\nThat's all folks!"
