# Purpose: Count how many times each word appears in user input.
# Concepts: Lists, while loops, break, input, .strip(), .lower(), .append(),
# Counter, imports, .items(), and f-strings.

from collections import Counter

values = input("Enter your words: ").strip()
words = values.split()
word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"{word}: {count}")