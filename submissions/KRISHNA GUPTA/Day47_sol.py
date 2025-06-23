n=list(map(int, input("Enter signal (space-separated): ").split()))
w=int(input("Enter window size (W): "))
smoothed_signal=[]

for i in range(len(n)-w+1):
    x = n[i:i+w]
    average = sum(x) // w
    smoothed_signal.append(average)
    i += 1

print("Smoothed Signal:", *smoothed_signal)