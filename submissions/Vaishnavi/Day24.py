numbers = list(map(int, input("Enter numbers: ").split()))
message = ''.join(chr(num) for num in numbers)
print("Decoded Message:", message)