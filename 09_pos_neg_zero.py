#Positive, Negative, or Zero: Determine if a number is positive, negative, or zero.

print("Determine if a number is positive, negative, or zero")
num = float(input("Enter a number: "))
if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print("Number is zero")
