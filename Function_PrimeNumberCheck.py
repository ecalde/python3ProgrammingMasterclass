# Prime numbers are numbers that cam only be cleanly divided by themselves and 1.
# Write a function that checks whether if the number is pased into a prime number or not.

def prime_checker(number):
    if number == 1:
        print("It's not a prime number")
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("It's not a prime number")
                break
        else:
            print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
