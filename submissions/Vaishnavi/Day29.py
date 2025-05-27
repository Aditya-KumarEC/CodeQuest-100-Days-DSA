list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
common = set(list1) & set(list2)
if common:
    print("Common elements:", ' '.join(map(str, common)))
else:
    print("No common elements found.")
   