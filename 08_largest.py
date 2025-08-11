# Largest of Three: Find the largest number among three numbers entered by the user.

print("Largest number among 3 numbers entered by user")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1>=num2 and num1>=num3:
    print("First number",num1,"is greater than",num2,"and",num3)
elif num1<=num2 and num3<=num2:
    print("Second number",num2,"is greater than",num1,"and",num3)
else:
    print("Third number",num3,"is greater than",num1,"and",num2)
