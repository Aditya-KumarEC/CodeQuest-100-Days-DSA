N = input("Enter N: ")
even_digits = []
for digit in N:
    if int(digit) % 2 == 0:
        even_digits.append(digit)
        
if even_digits:
    print("Even digits:", ' '.join(even_digits))
else:
    print("No even digits found!")
 

    