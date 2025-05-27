def decode_caesar(text,shift):
    decoded = ""
    for char in text:
        if char.isupper():
            pos = ord(char)- ord('A')
            new_pos = (pos - shift) % 26
            decoded_char = chr(ord('A') + new_pos)
            decoded += decoded_char
        elif char.islower():
            pos = ord(char) - ord('a')
            new_pos = (pos-shift) % 26
            decoded_char = chr(ord('a') + new_pos)
            decoded += decoded_char
        else:
            decoded += char
    return decoded

cipher = input("Enter cipher text: ")
shift = int(input("Enter shift value: "))

original = decode_caesar(cipher,shift)
print("Decoded Message: ",original)


