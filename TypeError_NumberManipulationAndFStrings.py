# you can round your division, second space is the number of decimal places you wish to round to
print(round(2.666666, 2))
# regular division leaves a remainder
print(type(8 / 3))
# floor division creates it into an int. This is handy to use so you don't have to use int conversion
print(type(8 // 3))
# f-string does all of the converting without you having to type all the extra stuff
score = 0
height = 1.8
isWinning = True
# you have to use the {curly braces} to utilize f-string and make string interpolation simpler
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
