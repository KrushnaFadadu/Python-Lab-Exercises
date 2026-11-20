
# Dice Simulator Using Random Module

import random

print("===== DICE SIMULATOR =====")

while True:

    input("\nPress Enter to roll the dice...")

    dice = random.randint(1, 6)

    print("You rolled:", dice)

    if dice == 1:
        print("You got ONE!")

    elif dice == 6:
        print("Congratulations! You got SIX!")

    else:
        print("Try again!")

    choice = input("\nDo you want to roll again? (yes/no): ")

    if choice.lower() != "yes":

        print("Thank you for playing!")

        break
