fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cheries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
# list on index 0 is the whole fruits list
# list on index 1 is the whole vegetables list
print(dirty_dozen[0])
print(dirty_dozen[1])
# the second square bracket is the index inside that nested index
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])