

import random

def hangman():
    words = ["python", "hangman", "github", "program", "code"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        guessed_letters.append(guess)

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

hangman()
