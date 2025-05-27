cipher_text = input("Enter cipher text: ")
shift = int(input("Enter shift value: "))
def decode_char(c, shift):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base - shift) % 26 + base)
    return c
decoded = ''.join(decode_char(c, shift) for c in cipher_text)
print("Decoded Message:", decoded)