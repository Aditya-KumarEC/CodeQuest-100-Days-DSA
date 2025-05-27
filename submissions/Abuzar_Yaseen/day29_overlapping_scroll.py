list1 = input("Enter first list: ").split()
list2 = input("Enter second list: ").split()
set1 = set(int(x) for x in list1)
set2 = set(int(x) for x in list2)
common = set1.intersection(set2)
if common :
    print("Common elements: ",*sorted(common))
else:
    print("No common elements found!")

