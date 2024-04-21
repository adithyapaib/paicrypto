from Crypto.Util.number import getPrime, inverse

# Generate random prime numbers p and g
p = getPrime(1024)
g = 2

# Generate private key
x = 12345

# Calculate public key
y = pow(g, x, p)

# Encryption
def encrypt(plaintext):
    # Generate random value k
    k = 54321

    # Calculate c1 and c2
    c1 = pow(g, k, p)
    c2 = (plaintext * pow(y, k, p)) % p

    return c1, c2

# Decryption
def decrypt(c1, c2):
    # Calculate shared secret
    shared_secret = pow(c1, x, p)

    # Calculate inverse of shared secret
    inv_shared_secret = inverse(shared_secret, p)

    # Calculate plaintext
    plaintext = (c2 * inv_shared_secret) % p

    return plaintext

# Example usage
plaintext = 42
c1, c2 = encrypt(plaintext)
decrypted_plaintext = decrypt(c1, c2)

print("Plaintext:", plaintext)
print("Encrypted:", (c1, c2))
print("Decrypted:", decrypted_plaintext)