# Problem 16: Character Frequency



myString = input("Enter a string: ")

frequency = {}

myString = myString.lower()

for character in myString:

    if character in frequency:
        frequency[character] += 1

    else:
        frequency[character] = 1

print(frequency)