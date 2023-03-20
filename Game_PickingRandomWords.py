import random
word_list = ["aardvark", "baboon", "camel"]

# To Do - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# random = random.randint(0,3)
# chosen_word = word_list[random]
chosen_word = random.choice(word_list)

# To Do - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# To Do - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#for letter in range(0, len(chosen_word)):
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
