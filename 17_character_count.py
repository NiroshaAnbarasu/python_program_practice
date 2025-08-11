# Character Counter: Count the number of vowels and consonants in a string.

print("Count the number of Vowels and Consonants in a given string")
text = (input("Enter a string: "))
vowels = consonants= 0
for ch in text:
    if ch.isalpha():
        if ch in ('aeiou'):
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
