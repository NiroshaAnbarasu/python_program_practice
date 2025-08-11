# Create a program that takes two numbers and an operator (+, -, *, /) and performs the calculation

print("Arithmetic operations")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter one operator +,-,*,/: ")
print("Given numbers are: First Number =",num1, ", Second Number =",num2)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

print(f"Result: {result}")
