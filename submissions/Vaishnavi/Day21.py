numbers = list(map(int, input("Enter numbers: ").split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Output:", even_sum)