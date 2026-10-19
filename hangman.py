
import random


with open("words.txt", "r") as file:
    words = [line.strip().lower() for line in file if line.strip()]


word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("   HANGMAN WORD GUESSING GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 wrong guesses allowed.")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won! 🎉")
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess! ✅")
    else:
        wrong_guesses += 1
        print("Wrong guess! ❌")

else:
    print("\nGame over!")
    print("The correct word was:", word)

print("\nThanks for playing!")
