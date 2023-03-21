import math

# Define a function called paint_calc() so that the code below works.
def paint_calc(height, width, cover):
    print("You'll need " + str(math.ceil(height * width / cover)) + " cans of paint." )

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

