from functions import hasThreeDifferentVowels
from functions import removeAccents

print("Enter your text (end input with a line ending in '*'):")
lines = []
while True:
    line = input()
    lines.append(line)
    if line.endswith('*'):
        break

text = ' '.join(lines).replace('*', '').strip().lower()
text = removeAccents(text)

words = [w.strip('.,;:!?') for w in text.split()]
words_with_vowels = [w for w in words if hasThreeDifferentVowels(w)]

print("\nWords with at least 3 different vowels:")
if len(words_with_vowels) > 0:
    for w in words_with_vowels:
            print("-", w)
else:
    print("None found.")

sentences = [s.strip() for s in text.split('.') if s.strip() != ""]
total_sentences = len(sentences)
print("\nTotal number of sentences:", total_sentences)

if total_sentences > 0:
    long_sentences = 0
    for s in sentences:
        if len(s.split()) > 5:
            long_sentences += 1
    percentage = (long_sentences * 100) / total_sentences
    print("Percentage of sentences with more than 5 words: {:.2f}%".format(percentage))
else:
    print("No sentences found.")