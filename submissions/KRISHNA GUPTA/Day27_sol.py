n=input("Enter module scores (space-separated): ")
numbers = list (map(int, n.split()))
lst=[]
for i in numbers:
    if i <50:
        lst.append(i)


if lst:
    print("Modules to debug:", end =" ".join(map(str, lst)))
else:
    print("All modules are working fine!")