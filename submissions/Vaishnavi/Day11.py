numbers = input("Enter numbers separated by spaces: ")
str_list = numbers.split()
number_list = []
for num in str_list:
    number_list.append(int(num))
number_list.sort()
print("Sorted list:", number_list)