# Factorial Calculator: Calculate the factorial of a number using a loop.

print("Calculate the factorial")

num = int(input("Enter a number: "))

fact = 1

if num > 0:
    for i in range (1 , num+1):
        fact *= i
    print(f"Factorial of {num} is: {fact}")
else:
    print("Please enter a positive integer.")
