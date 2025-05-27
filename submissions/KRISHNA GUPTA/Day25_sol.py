n=input("Enter a Sentence: ")
words=n.split()
longest_word=max(words, key=len)
print("Longest Word:", longest_word)