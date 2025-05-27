password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True

missing = []
if not has_upper:
    missing.append("uppercase letter")
if not has_lower:
    missing.append("lowercase letter")
if not has_digit:
    missing.append("digit")
if not has_special:
    missing.append("special character")

if has_upper and has_lower and has_digit and has_special:
    print("\nStrong Password")
else:
    print("\nWeak Password (Missing " + " and ".join(missing) + ")")