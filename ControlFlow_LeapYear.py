# Calculate leap year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0 and year % 400:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")