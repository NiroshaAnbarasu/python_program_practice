# Even or Odd: Write a program that determines if a number is even or odd

print("Determine a number is even or odd")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The given number",num,"is even")
else:
    print("The given number",num,"is odd")
