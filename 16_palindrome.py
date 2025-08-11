# Palindrome Checker: Check if a word or phrase is a palindrome (reads the same forwards and backwards).

print("Check if a word or phrase is a Palndrome")
while True:
    text = input("Enter a word or phrase (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Exiting Palindrome Checker")
        break

    # to remove space,characterss,symbols
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    # reverse
    reversed_text = ""
    for char in cleaned:
        reversed_text = char + reversed_text

    # Check palindrome
    if cleaned == reversed_text:
        print(f"{text} is a palindrome!\n")
    else:
        print(f"{text} is NOT a palindrome.\n")
