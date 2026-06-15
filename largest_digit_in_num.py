# Problem 9: Take a number and print the largest digit.



num = input("Enter a number: ")

largest = 0

for digit in num:

    current = int(digit)

    if current > largest:

        largest = current

print(f"largest: {largest}")




    



    

