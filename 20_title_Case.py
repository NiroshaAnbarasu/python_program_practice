# Title Case Converter: Convert a string to title case (first letter of each word capitalized).

print("Convert a string to title case (first letter of each word capitalized)")
text = input("Enter a sentence: ")

# without .title()
words = text.split()
title_word = [word[0].upper() + word[1:].lower() if len(word) > 0 else "" for word in words]
title_text = " ".join(title_word)
print("Title Case without .title():", title_text)

# with .title()
print("Title Case with .title():", text.title())
