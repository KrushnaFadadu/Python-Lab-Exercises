
# Frequency Counter Using Dictionaries

text = input("Enter a sentence: ")

frequency = {}

for character in text:

    if character != " ":

        if character in frequency:

            frequency[character] += 1

        else:

            frequency[character] = 1

print("\n===== CHARACTER FREQUENCY =====")

for character, count in frequency.items():

    print(character, ":", count)
