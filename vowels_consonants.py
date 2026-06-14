# Problem 7: Take a character as input and check whether it is a vowel or a consonant



char = input("Enter a character: ")

if not char.isalpha() or len(char) != 1:
    print("Invalid Character!")   

elif char.lower() in "aeiou":
    print("Vowel")

else:
    print("Consonant")