# List Sum and Average: Calculate the sum and average of numbers in a list.

print("List Sum and Average: Calculate the sum and average of numbers in a list")

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

total_sum = 0
for num in numbers:
    total_sum += num

average = total_sum / len(numbers) if len(numbers) > 0 else 0

print("Numbers:", numbers)
print("Sum:", total_sum)
print("Average:", average)
