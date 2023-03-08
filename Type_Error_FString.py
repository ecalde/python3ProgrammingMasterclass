# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age? ")

# 1 year = 365 days / 1 year = 52 weeks / 1 year = 12 months / 90 years max
ageAsInt = int(age)
yearsLeft = 90 - ageAsInt
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365
print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")



