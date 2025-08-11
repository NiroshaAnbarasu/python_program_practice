#String Reverser: Reverse a string without using built-in reverse functions.

print("Reverse a string without using built-in reverse functions")
text= input("Enter a string: ")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Prepend each character

print("Reversed string:", reversed_text)
