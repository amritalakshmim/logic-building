# Problem 3: Take two numbers as input and print which number is larger.



num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger")

elif num2 > num1:
    print(f"{num2} is larger")

else:
    print("Both are equal")