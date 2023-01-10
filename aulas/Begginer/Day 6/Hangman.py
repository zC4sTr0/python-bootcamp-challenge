import random

word_list = ["aardvark", "baboon", "camel", "stark",
             "joaozinho", "gabriel", "apple", "banana"]
chosen_word = random.choice(word_list)
display_word = chosen_word

# Testing code
print(f'DEBUG: The word choosen is: "{chosen_word}".')

for letter_display in chosen_word:
    print("_", end=" ")
    display_word = display_word.replace(letter_display, "_")

letter_guesses = input("\nGuess a letter: ").lower()

for letter in range(len(chosen_word)):
    if letter_guesses == chosen_word[letter]:
        display_word = display_word[:letter] + \
            letter_guesses + display_word[letter + 1:]

print(display_word)
