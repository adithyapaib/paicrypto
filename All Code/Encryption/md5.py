import hashlib


plainText = input("Enter the text to hash: ")
hash_object = hashlib.md5(plainText.encode())
print("The MD5 hash is:", hash_object.hexdigest())