def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = "HELLO"
shift = 3

encrypted = encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)
