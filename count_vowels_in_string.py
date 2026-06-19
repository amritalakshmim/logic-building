# Problem 15: Count Vowels in a String



word = input("Enter a string: ")

vowel_count = 0

for letter in word:

    if letter.lower() in "aeiou":

        vowel_count += 1

print(f"Count of vowels: {vowel_count}")
