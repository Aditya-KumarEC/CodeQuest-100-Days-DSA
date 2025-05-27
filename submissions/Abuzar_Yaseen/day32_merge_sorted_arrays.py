A = list(map(int,input("Enter first sorted array: ").split()))
B = list(map(int,input("Enter second sorted array: ").split()))
i = 0
j = 0
merged = []

while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i = i+1
        else:
            merged.append(B[j])
            j =j+1

while i < len(A):
        merged.append(A[i])
        i = i+1
while j < len(B):
        merged.append(B[j])
        j = j+1
print (*merged)
