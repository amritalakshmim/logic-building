# Problem 8: Take a character as input and determine whether it is Alphabet, Digit or Special Character



char = input("Enter a character: ")

if len(char) != 1:
    print("Invalid Character!")

elif char.isalpha():
    print("Alphabet")

elif char.isdigit():
    print("Digit")

else:
    print("Special character")
   