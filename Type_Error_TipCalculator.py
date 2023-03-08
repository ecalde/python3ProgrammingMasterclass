# Calculator that takes total bill, tip percentage, and the number of people
# Then it uses f-string to display how much each person will pay
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

totalPay = (total * ((percent / 100) + 1))
eachPay = totalPay / people

print(f"Each person should pay: ${eachPay:.2f}")