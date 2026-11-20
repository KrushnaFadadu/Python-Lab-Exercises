
# Number Guessing Game

import random

secret_number = random.randint(1, 100)

attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100.")

while True:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("\nCongratulations! You guessed correctly.")
        print("Secret Number:", secret_number)
        print("Total Attempts:", attempts)
        break
