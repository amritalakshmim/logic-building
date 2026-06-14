# Problem 6: Take a year and check whether it is a leap year.



year = int(input("Enter an year: "))

if year % 400 == 0:
    print("Leap year")

elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")

else:
    print("Not a leap year")