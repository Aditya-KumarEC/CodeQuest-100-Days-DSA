no=int(input("ener the number"))
fact=1
if no<0:
    print("factorial is not possible")
else:
    for i in range (1,no+1):
        fact=fact*i
    print(fact)
    
    