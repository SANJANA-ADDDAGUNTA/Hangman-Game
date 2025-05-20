import random

def hangman():
    words = ["python", "internship", "project", "automation"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in guessed:
        print(f"Word: {guessed}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed.")
        elif guess in word:
            guessed_letters.append(guess)
            guessed = "".join([char if char in guessed_letters else "_" for char in word])
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()
