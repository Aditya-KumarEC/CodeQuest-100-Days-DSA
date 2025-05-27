score = input("Enter module scores (space-separated): ")
score_list = list(map(int,score.split()))
threshold = 50
buggy = []
for score in score_list:
    if score < threshold:
        buggy.append(score)

if buggy:
    print("Module to debug: ",*buggy)
else:
    print("All modules are working fine")