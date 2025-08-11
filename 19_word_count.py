# Word Counter: Count the number of words in a sentence.

print("Count the number of words in a sentence")

text = input("Enter a sentence: ")
words = text.split()
word_count = len(words)
print("Number of words:", word_count)
