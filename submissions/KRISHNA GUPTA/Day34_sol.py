n=list(map(int, input("Input: Enqueue ").split()))
x=int(input("Dequeue"))
for i in range(min(x,len(n))):
    n.pop(0)
print(*n)