scores = list(map(int, input("Enter module scores (space-separated): ").split()))
buggy_modules = [score for score in scores if score < 50]
print("Modules that need fixing:", buggy_modules)