# CTI 110
# P4LAB1 - Part B
# Text "graphics"
# Clemons
# 10/5/23

# Draw a rectangle
CHAR = "😈"
#print(CHAR)

# Part 1: Draw a horizontal line
WIDTH = int(input("How wide is the rectangle?"))
HEIGHT = int(input("How tall is it?"))

                   
print("Printing", WIDTH, "columns")
for column in range(WIDTH):
    #don't go to newline
    print(CHAR, end="")
print()

# Part 2: Verticle line
for row in range(HEIGHT):
    print(CHAR) # we want the newline
# Part 3: Draw the rectangle

for row in range(HEIGHT):
    for column in range(WIDTH):
        print(CHAR, end="")
    print() # end the line
    
