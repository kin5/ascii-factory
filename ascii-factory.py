# ascii-factory
# Kinman Covey
# 3/2/2015

from PIL import Image
import sys

run = True
while run != False:
    # Get a filename, and a scale
    # Create the image object and print out its dimensions
    filename = raw_input("Enter filename (or stop to exit): ")
    if filename == "stop":
        run = False
        break
    
    while True:
        try:
            image = Image.open(filename)
            break
        except IOError:
            filename = raw_input("Incorrect filename, enter again (or stop to exit): ")

    print "\nThis next value is how much you want to scale each dimension down by (because the image is more than likely very large)."
    print "I've found scale_x = 10 and scale_y = 20 works well, but any 1x2 dimension would probably be fine."
    scale_x = input("Enter the down scale x value (5, 2, etc): ")
    scale_y = input("Enter the down scale y value (10, 4, etc): ")

    # Open text file for output
    text_file = open(filename + ".txt", "w")
        
            
    print "Image size: " + str(image.size)

    w, h = image.size
        
    obj = image.load()

    # Data section
    # List RGB vars
    r_list = []
    g_list = []
    b_list = []

    # Average RGB vars
    r_avg = 0
    g_avg = 0
    b_avg = 0
    i_avg = 0

    # Minimum RGB vars
    r_min = 255
    g_min = 255
    b_min = 255

    # Overall count var
    count = 0

    print "Finding RGB floors..."
    # Find the minimum r, g, and b value for testing purposes
    # Found out picture that were really light were not decipherable
    # Added this to detect minimum of each and use that as the floor
    for i in range(0, h):
        for j in range(0, w):
            if len(obj[j,i]) == 3:
                r, g, b = obj[j,i]
            elif len(obj[j,i]) == 4:
                r, g, b, a = obj[j,i]
            if r < r_min:
                r_min = r

            if g < g_min:
                g_min = g

            if b < b_min:
                b_min = b

            # Analytical data
            if r > g and r > b:
                r_list.append(r)
            elif g > r and g > b:
                g_list.append(g)
            elif b > r and b > g:
                b_list.append(b)

            count += 1


    print "Finding averages..."
    #Find the averages
    for i in range(0, len(r_list)):
        r_avg += r_list[i]

    for i in range(0, len(g_list)):
        g_avg += g_list[i]

    for i in range(0, len(b_list)):
        b_avg += b_list[i]

    print len(r_list)

    i_avg = (r_avg + g_avg + b_avg) / count
    if len(r_list) > 0:
        r_avg = r_avg / len(r_list)
    if len(g_list) > 0:
        g_avg = g_avg / len(g_list)
    if len(b_list) > 0:
        b_avg = b_avg / len(b_list)

    print "Printing picture..."
    # And here's where the magic happens
    for i in range(0, h):
        for j in range(0, w):
            if i % scale_y == 0 and j % scale_x == 0:
                if len(obj[j,i]) == 3:
                    r, g, b = obj[j,i]
                elif len(obj[j,i]) == 4:
                    r, g, b, a = obj[j,i]
                    
                if r <= r_min + 25 and g <= g_min + 25 and b <= b_min + 25:
                    sys.stdout.write("#")
                    text_file.write("#")
                elif r <= r_min + 50 and g <= g_min + 50 and b <= b_min + 50:
                    sys.stdout.write("%")
                    text_file.write("%")
                elif r <= r_min + 75 and g <= g_min + 75 and b <= b_min + 75:
                    sys.stdout.write("I")
                    text_file.write("I")
                elif r <= r_min + 100 and g <= g_min + 100 and b <= b_min + 100:
                    sys.stdout.write("i")
                    text_file.write("i")
                elif r <= r_min + 125 and g <= g_min + 125 and b <= b_min + 125:
                    sys.stdout.write("!")
                    text_file.write("!")
                elif r <= r_min + 150 and g <= g_min + 150 and b <= b_min + 150:
                    sys.stdout.write("+")
                    text_file.write("+")
                elif r <= r_min + 175 and g <= g_min + 175 and b <= b_min + 175:
                    sys.stdout.write(":")
                    text_file.write(":")
                elif r <= r_min + 200 and g <= g_min + 200 and b <= b_min + 200:
                    sys.stdout.write("-")
                    text_file.write("-")
                elif r <= r_min + 225 and g <= g_min + 225 and b <= b_min + 225:
                    sys.stdout.write("'")
                    text_file.write("'")
                elif r >= r_min + 250 and g >= g_min + 250 and b >= b_min + 250:
                    sys.stdout.write(" ")
                    text_file.write(" ")
                elif r > b and g > b and r > r_avg and g > g_avg: # Yellows
                    sys.stdout.write("`")
                    text_file.write("`")
                elif r > g and b > g and r > r_avg and b > b_avg: # Purps
                    sys.stdout.write("%")
                    text_file.write("%")
                elif g > r and b > r and g > g_avg and b > b_avg: # Cyans
                    sys.stdout.write(";")
                    text_file.write(";")
                elif r > g and r > b and r > r_avg: # Reds 
                    sys.stdout.write("$")
                    text_file.write("$")
                elif g > r and g > b and g > g_avg: # Greens 
                    sys.stdout.write(",")
                    text_file.write(",")
                elif b > g and b > r and b > b_avg: # Blues
                    sys.stdout.write("\"")
                    text_file.write("\"")
                else:
                    sys.stdout.write(".")
                    text_file.write(".")
        if i % scale_y == 0:
            print
            text_file.write("\n")

    text_file.close()
    print "Avg R: " + str(r_avg)
    print "Avg G: " + str(g_avg)
    print "Avg B: " + str(b_avg)
    print "AVG RGB: " + str(i_avg)

    # We're done here
    print "\nThat's all folks!\n"

