# Problem 14: Palindrome Number-A number is a palindrome if it reads the same forward and backward.



number = input("Enter a number: ")

reverse = ""

for digit in number:
    
    reverse = digit + reverse

if reverse == number:
    print("Palindrome")

else:
    print("Not palindrome")    