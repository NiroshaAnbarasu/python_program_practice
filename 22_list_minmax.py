# List Maximum and Minimum: Find the maximum and minimum values in a list without using built-in functions.

print("List Maximum and Minimum: Find the maximum and minimum values in a list without using built-in functions")

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum=num
    if num < minimum:
        minimum=num
print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
