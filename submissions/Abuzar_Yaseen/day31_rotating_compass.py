rotaion = input("Enter numbers: ")
arr = [int(x) for x in rotaion.split()]
K = int(input("Enter rotation value(K): "))
K = K % len(arr)
rotated_array = arr[-K:] + arr[:-K]
print("Rotated Array: ",*rotated_array)