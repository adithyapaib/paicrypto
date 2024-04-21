from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return cipher.iv + ciphertext

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Take input from user
key = input("Enter the key: ").encode()
plaintext = input("Enter the plaintext: ").encode()

# Check if plaintext or key is smaller than block size
if len(plaintext) < AES.block_size:
    plaintext = pad(plaintext, AES.block_size)
if len(key) < AES.block_size:
    key = pad(key, AES.block_size)

ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
print("Used Key:", key.decode())
