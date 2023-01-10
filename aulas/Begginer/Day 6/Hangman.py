import random

word_list = ["aardvark", "baboon", "camel", "stark", "joaozinho", "gabriel"]

letter = input("Guess a letter: ").lower()

for word in word_list:
    position = word.find(letter)
    if (position != -1):
        print("Found in word: " + word)
    else:
        print("Not found in word: " + word)
