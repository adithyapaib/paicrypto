from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Get public and private keys
public_key = key.publickey()
private_key = key

# Get user input
message = input("Enter the message to encrypt: ")

# Encrypt the message
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message.encode())

# Decrypt the message
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message).decode()

# Display the results
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)