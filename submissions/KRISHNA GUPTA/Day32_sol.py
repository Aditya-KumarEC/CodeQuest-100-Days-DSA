n1=list(map(int, input("Enter first sorted array:").split()))
n2=list(map(int, input("Enter second sorted array:").split()))
lst=[]
for i in n1:
    lst.append(i)
for j in n2:
    lst.append(j)
lst.sort()
print("Merged Sorted Array:",*lst)