n=input("Enter a Sentence: ").lower()
vowels = "aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
v=0
c=0
for i in n:
    if i in vowels:
        v+=1
    elif i in consonants:
        c+=1

print("Vowels:", v)
print("Consonants:",c)