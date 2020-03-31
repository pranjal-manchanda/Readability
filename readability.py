"""
Program takes in an input string and outputs its corresponding grade level
using the Coleman-Liau method.

Input: Any text
Output: Grade level of the input
"""

import string

text = input("Text: ")  # Request input string

# Initialize variables
letters, words, sentences = 0, 0, 0

# Iterate over each letter of input string
for char in text:
    # Count letters
    if char in string.ascii_letters:
        letters += 1
    # Count sentences
    elif char in ['.', '?', '!']:
        sentences += 1

# Compute number of words
words = len(text.split())

# print(letters, words, sentences)

avgLetters = (100/words) * letters  # Average letters per hundred words
avgSentences = (100/words) * sentences  # Average sentences per hundred words

grade = (.0588 * avgLetters) - (.296 * avgSentences) - 15.8  # Coleman-Liau formula

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(grade)}")