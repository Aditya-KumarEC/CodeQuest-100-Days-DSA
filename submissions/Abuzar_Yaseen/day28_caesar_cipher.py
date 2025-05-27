text = input("Enter cipher text: ")
shift = int(input("Enter shift value: "))
result = ""
for char in text:
    if 'A' <= char <= 'Z':
        pos = ord(char) - ord('A')
        new_pos = (pos - shift) % 26
        result += chr(new_pos+ ord('A'))
    elif 'a' <= char <= 'z':
        pos = ord(char) - ord('a')
        new_pos = (pos - shift) % 26
        result += chr(new_pos + ord('a'))
    else:
        result += char
print("Decoded: ",result)
