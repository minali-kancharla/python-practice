# Purpose: Count how many times each word appears in user input.
# Concepts: Lists, while loops, break, input, .strip(), .lower(), .append(),
# Counter, imports, .items(), and f-strings.

from collections import Counter

words = []

while True:
    values = input("Enter your words. Type 'quit' as the key to finish: ").strip()
    
    if values.lower() == 'quit':
        break   
        
    words.append(values)

word_counts = Counter(words)
for word, count in word_counts.items():
    print(f"{word}: {count}")