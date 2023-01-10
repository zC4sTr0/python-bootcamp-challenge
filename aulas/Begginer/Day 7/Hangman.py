import random

word_list = ["aardvark", "baboon", "camel", "stark",
             "joaozinho", "gabriel", "apple", "banana"]
chosen_word = random.choice(word_list)
display_word = []

for _ in range(len(chosen_word)):
    display_word += "_"

# Testing code
print(f'DEBUG: The word choosen is: "{chosen_word}".')


while ("".join(display_word) != chosen_word):
    letter_guesses = input("\nGuess a letter: ").lower()
    for _ in range(len(chosen_word)):
        if (chosen_word[_] == letter_guesses):
            display_word[_] = letter_guesses
    print(display_word)

print("You win!")
