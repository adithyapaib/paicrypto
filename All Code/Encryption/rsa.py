from rsa_python import rsa

keypair = rsa.generate_key_pair(1024)
plaintext = input("Enter the plaintext: ")
encrypted = rsa.encrypt(plaintext, keypair["public"], keypair["modulus"])
print("Encrypted:", encrypted)

decrypted = rsa.decrypt(encrypted, keypair["private"], keypair["modulus"])
print("Decrypted:", decrypted)
