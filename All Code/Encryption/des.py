from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt(key, plaintext):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext.hex()

def decrypt(key, ciphertext):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_text = cipher.decrypt(bytes.fromhex(ciphertext))
    plaintext = unpad(decrypted_text, DES.block_size).decode()
    return plaintext

def main():
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    # Fix key length
    if len(key) < 8:
        key = key.ljust(8, '0')
    elif len(key) > 8:
        key = key[:8]

    # Pad plaintext if needed
    if len(plaintext) % 8 != 0:
        plaintext = pad(plaintext.encode(), DES.block_size).decode()

    ciphertext = encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()