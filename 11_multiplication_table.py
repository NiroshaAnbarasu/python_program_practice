# Multiplication Table: Print the multiplication table for a number entered by the user.

print("Multiplication Table")
num = int(input("Enter a number to print multiplication table: "))

for i in range(1 , 11):
    res = num * i
    print(f"{num} * {i} = {res}")
