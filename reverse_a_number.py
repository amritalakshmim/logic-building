# Problem 13: Reverse a Number



num = input("Enter a number: ")

reverse = ""

for digit in num:

    reverse = digit + reverse

print(f"Reversed number: {reverse}")