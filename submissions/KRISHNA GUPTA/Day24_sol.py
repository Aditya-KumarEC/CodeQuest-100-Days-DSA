n=input("Enter numbers: ")
numbers = list(map(int, n.split()))
print("Decoded Message: ", end="")
for i in numbers:
    {
        print (chr(i),end="")
    }