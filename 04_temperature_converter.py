#   Convert temperatures between Celsius and Fahrenheit. Ask the user which conversion they want.
#   Fahrenheit to Celsius: °C = (°F - 32) × 5/9
#   Celsius to Fahrenheit: °F = (°C × 9/5) + 32

print("Which conversion you want to perform?")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
ch = input( "Enter 1 or 2: ")

if ch == "1":
    fahrenheit = float(input("Fahrenheit teemperature: "))
    celcius = (fahrenheit - 32) * (5 / 9)
    print("Celcius: ", celcius)

elif ch == "2":
    celsius = float(input("Celsius temperature: "))
    fahrenheit=(celsius * (9/5) + 32)
    print("Fahrenheit: ", fahrenheit)

else:
    print("Invalid choice")
