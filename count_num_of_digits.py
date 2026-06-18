# Problem 11: Take a number and print how many digits it contains



num = input("Enter a number: ")

count = 0

for digit in num:
    count += 1

print(f"Number of digits: {count}")
