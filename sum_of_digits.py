# Problem 10: Take a number and find the sum of all digits.



num = input("Enter a number:")

sum = 0

for digit in num:

    current = int(digit)

    sum += current

print(f"Sum: {sum}")