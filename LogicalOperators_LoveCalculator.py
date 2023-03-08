# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
name1Lower = name1.lower()
name2Lower = name2.lower()
firstTCount = (name1Lower.count("t")) + (name2Lower.count("t"))
firstRCount = (name1Lower.count("r")) + (name2Lower.count("r"))
firstUCount = (name1Lower.count("u")) + (name2Lower.count("u"))
firstECount = (name1Lower.count("e")) + (name2Lower.count("e"))
secondLCount = (name1Lower.count("l")) + (name2Lower.count("l"))
secondOCount = (name1Lower.count("o")) + (name2Lower.count("o"))
secondVCount = (name1Lower.count("v")) + (name2Lower.count("v"))
secondECount = (name1Lower.count("e")) + (name2Lower.count("e"))
firstNum = firstTCount + firstRCount + firstUCount + firstECount
secondNum = secondLCount + secondOCount + secondVCount + secondECount
total = int(str(firstNum) + str(secondNum))

if total < 10 or total > 90:
    print(f"Your score is {total} you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

#Write your code below this line 👇
