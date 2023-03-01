#Check data type of two_digit_number
two_digit_number = input("Type a two digit number: ")
# Get the first and second digits using subscripting then convert string to int.
first = int(two_digit_number[0])
second = int(two_digit_number[1])
print(first + second)
