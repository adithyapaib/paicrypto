import hashlib

def calculate_sha256_hash(string):
    sha256_hash = hashlib.sha256(string.encode()).hexdigest()
    return sha256_hash

# Example usage
input_string = "Hello, world!"
sha256_hash = calculate_sha256_hash(input_string)
print("SHA-256 hash:", sha256_hash)