
text = input("Enter text: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_text = ""
for char in text:
    if char not in punctuations:
        clean_text += char
words = clean_text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}")
