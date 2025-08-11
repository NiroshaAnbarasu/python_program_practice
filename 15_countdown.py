# Countdown Timer: Create a countdown from a given number to zero.

print("Countdown from a given number to zero")
num = int(input("Enter a number: "))
res = 0
if num > 0:
    for i in range (num, -1, -1):
        print(i)
