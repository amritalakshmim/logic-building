# Problem 12: Take a number and count how many even digits it contains.



num = input("Enter a number: ")

even_count = 0

for digit in num:
    current = int(digit)

    if current % 2 == 0:
        even_count += 1

print(f"Count of even digits: {even_count}")