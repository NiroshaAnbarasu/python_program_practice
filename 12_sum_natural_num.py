# Sum of Natural Numbers: Calculate the sum of first n natural numbers where n is provided by the user.
#  sum = (n(n+1))/2

print("Sum of First n natural numbers")
num = int(input("Enter a number: "))
sum = 0
if num > 0:
   # sum = (num * (num + 1)) / 2
   # print(f"Sum of first {num} natural numbers is {sum}")

    for i in range(1, num + 1):
        sum += i
    print(f"The sum of the first {num} natural numbers is: {sum}")
else:
    print("Please enter a positive integer.")
