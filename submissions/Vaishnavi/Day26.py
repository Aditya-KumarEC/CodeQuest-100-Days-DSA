sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0
vowel_set = "aeiouAEIOU"
for char in sentence:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)