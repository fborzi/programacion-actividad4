from functions import repeatedLetters

text = input("Enter a text: ")
    
words = text.split()
print(f"\nTotal number of words in the text: {len(words)}\n")
    
for word in words:
    repeated = repeatedLetters(word)
    if repeated:
        print(f"In the word '{word}', the repeated letters are: {', '.join(sorted(repeated))}")
    else:
        print(f"In the word '{word}', there are no repeated letters.")