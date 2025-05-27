n=list(map(int, input("Input: Push ").split()))
x=int(input("Pop "))
for i in range(min(x, len(n))):
    n.pop()

print(*n)