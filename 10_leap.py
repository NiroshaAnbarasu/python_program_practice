# Leap Year Checker: Determine if a given year is a leap year.

print("To Determine if a given year is a leap year")
year = int(input("Enter the year: "))
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
