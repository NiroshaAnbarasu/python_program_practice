# Number Guessing Game: Create a simple guessing game where the computer picks a random number between 1-100 and the user tries to guess it.

import random
print("Simple guessing game where the computer picks a random number between 1 - 100 and the user tries to guess it")
secret_num = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_num:
        print("Too low! Try again.")
    elif guess > secret_num:
        print("Too high! Try again.")
    else:
        print(f"Congrats! You guessed it in {attempts} attempts.")
        break
