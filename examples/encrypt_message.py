from algorithms.symmetric.caesar_cipher import encrypt

message = "Secret Message"
cipher = encrypt(message, 3)

print("Encrypted message:", cipher)
