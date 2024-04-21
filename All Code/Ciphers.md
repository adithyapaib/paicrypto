## Caesar Cipher

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. The shift value, also known as the key, determines the amount of shift for encryption and decryption.

### Encryption:
- Each letter in the plaintext is shifted forward in the alphabet by a fixed number of positions.
- For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.

### Decryption:
- Decryption is performed by shifting each letter in the ciphertext backward in the alphabet by the same fixed number of positions.

### Algorithm:
1. Convert each letter of the plaintext to its ASCII value.
2. Add the shift value to each ASCII value to get the encrypted ASCII value.
3. If the resulting ASCII value exceeds the range of alphabet characters, wrap around to the beginning of the alphabet.
4. Convert the encrypted ASCII values back to characters to obtain the ciphertext.

#### Example:
- Plaintext: "HELLO"
- Shift: 3
- Encrypted text: "KHOOR"

The Caesar cipher is straightforward to implement and understand but offers very little security, as there are only 25 possible keys to try. Despite its simplicity, it provides a foundation for more complex encryption techniques.

```
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # For uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # For lowercase letters
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            # For digits
            result += str((int(char) + shift) % 10)
        else:
            # For non-alphanumeric characters
            result += char

    return result

def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # For uppercase letters
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            # For lowercase letters
            elif char.islower():
                result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isdigit():
            # For digits
            result += str((int(char) - shift) % 10)
        else:
            # For non-alphanumeric characters
            result += char

    return result

def main():
    while True:
        plaintext = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        mode = input("Enter 'e' or 'd': ")

        if mode.lower() == "e":
            encrypted_text = caesar_encrypt(plaintext, shift)
            print("Encrypted text:", encrypted_text)
        elif mode.lower() == "d":
            decrypted_text = caesar_decrypt(plaintext, shift)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
    
```



## 2. Vigenère Cipher

The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It uses a keyword to determine the shift value for each letter in the plaintext. Here's how it works:

1. Choose a keyword.
2. Repeat the keyword to match the length of the plaintext.
3. Convert each letter of the keyword and the plaintext to numbers (A=0, B=1, ..., Z=25).
4. Add the corresponding numbers of the keyword and the plaintext, taking modulus 26.
5. Convert the resulting numbers back to letters.

### Encryption:
- The plaintext is encrypted by shifting each letter according to the corresponding letter in the keyword.

### Decryption:
- The ciphertext is decrypted by shifting each letter back according to the corresponding letter in the keyword.

The Vigenère cipher was considered unbreakable for several centuries but can be cracked through frequency analysis if the length of the keyword is known. However, it remains an important part of cryptographic history and serves as a foundation for understanding more complex encryption techniques.

![image](https://gist.github.com/assets/40488244/e394f2c1-bb09-4d2c-a7ad-c5f788d905ff)

### Code :


```
def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Convert character to uppercase
            char = char.upper()
            # Get the corresponding shift value from the key
            shift = ord(key[key_index]) - 65
            # Encrypt the character
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
            # Move to the next letter in the key
            key_index = (key_index + 1) % len(key)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Convert character to uppercase
            char = char.upper()
            # Get the corresponding shift value from the key
            shift = ord(key[key_index]) - 65
            # Decrypt the character
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
            # Move to the next letter in the key
            key_index = (key_index + 1) % len(key)
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char

    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()



```

## 3. Rail Fence Cipher

The Rail Fence cipher, also known as the Zigzag cipher, is a transposition cipher that rearranges the plaintext characters in a zigzag pattern. It encrypts the message by writing it in a diagonal pattern across a number of "rails" or "fences" and then reading off the letters row by row.

### Encryption:
1. Write the plaintext characters in a zigzag pattern across a specified number of rails (rows).
2. Read the characters row by row to generate the ciphertext.

### Decryption:
1. Calculate the number of characters in each rail based on the length of the ciphertext and the number of rails.
2. Write the ciphertext characters in the zigzag pattern across the rails.
3. Read off the characters diagonally to obtain the original plaintext.

### Algorithm:
- For encryption, iterate over the plaintext characters and fill the rails according to the zigzag pattern.
- For decryption, calculate the rail lengths based on the ciphertext length and the number of rails, then read off the characters diagonally to reconstruct the plaintext.

#### Example:
- Plaintext: "HELLO WORLD"
- Number of Rails: 3
- Encrypted text: "HOR LWLELODL"

The Rail Fence cipher provides a basic form of encryption that rearranges the characters of the plaintext, making it more difficult to read without the key. However, it is susceptible to frequency analysis and other cryptanalysis methods.

### Preview 
![image](https://gist.github.com/assets/40488244/9ab8f8d9-5a80-4cbb-a063-954a3885f53b)

```

def fence(lst, numrails):
    fence = [[None] * len(lst) for _ in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 0:  # debug
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]


def encode(text, n):
    return ''.join(fence(text, n))


def decode(text, n):
    rng = list(range(len(text)))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


text = input('Enter plain text = ')
mode = int(input("Enter rails (level) = "))
z = encode(text, mode)
print("Encoded:", z)
y = decode(z, mode)
print("Decoded:", y)

```
## 4. Columnar Transposition Cipher

The Columnar Transposition cipher is a transposition cipher that rearranges the plaintext characters by writing them into a grid and then reading them out column by column, based on a key. It's a simple and effective encryption technique that provides some level of security against casual interception.

### Encryption:
1. Write the plaintext characters into a grid row by row, following the specified number of columns determined by the length of the key.
2. Rearrange the columns of the grid alphabetically according to the characters of the key.
3. Read the characters column by column to generate the ciphertext.

### Decryption:
1. Arrange the columns of the grid back into their original order based on the characters of the key.
2. Read the characters row by row to obtain the original plaintext.

### Algorithm:
- For encryption, create a grid with the specified number of columns determined by the length of the key, then fill in the plaintext row by row. Rearrange the columns alphabetically according to the key.
- For decryption, rearrange the columns of the grid back to their original order based on the key, then read off the characters row by row.

#### Example:
- Plaintext: "HELLO WORLD"
- Key: "SECRET"
- Encrypted text: "LEOWHLRO LD"

The Columnar Transposition cipher provides a simple yet effective method of rearranging the characters of the plaintext to create ciphertext. While it's not as strong as modern encryption methods, it can offer some level of security for basic communication.


### Preview

![image](https://gist.github.com/assets/40488244/6c53bf99-4f3f-4550-8354-09ef4b2f6b0e)
![image](https://gist.github.com/assets/40488244/fe99d638-1869-4ec2-9800-dbb2d8b37f38)

```
import time
import math

# Encryption and Decryption functions for Columnar Transposition
def columnar_transposition_encrypt(text, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(text))
    msg_lst = list(text)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    return cipher

def columnar_transposition_decrypt(text, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(text))
    msg_lst = list(text)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot", "handle repeating words.")
    null_count = msg.count('_')
    if null_count > 0:
        return msg[:-null_count]
    return msg


def main_columnar_transposition():
    key = input("Enter the Columnar Transposition key: ")
    message = input("Enter the message to encrypt: ")

    # Encryption
    start_time = time.time()
    encrypted_message = columnar_transposition_encrypt(message, key)
    encryption_time = time.time() - start_time

    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the message? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_message = input("Enter the encrypted message: ")

        # Decryption
        start_time = time.time()
        decrypted_message = columnar_transposition_decrypt(encrypted_message, key)
        decryption_time = time.time() - start_time

        print(f"Decrypted message: {decrypted_message}")
        print(f"Decryption time: {decryption_time:.6f} seconds")

    avg_time = (encryption_time + decryption_time) / 2 if decrypt_choice.lower() == 'y' else encryption_time
    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_columnar_transposition()

#https://github.com/Auriel3003/Encryption-Techniques

```

## 5.RC4 Cipher

The RC4 (Rivest Cipher 4) is a symmetric stream cipher developed by Ron Rivest in 1987. It's widely used due to its simplicity and speed in both hardware and software implementations. RC4 encrypts data by generating a pseudorandom stream of bytes, which is then combined with the plaintext using the XOR operation.

### Encryption:
1. Initialize the RC4 cipher with a secret key (usually referred to as the RC4 key schedule).
2. Generate a stream of pseudorandom bytes using the key scheduling algorithm.
3. Apply the generated keystream to the plaintext using the XOR operation to produce the ciphertext.

### Decryption:
Since RC4 is a symmetric cipher, decryption is the same as encryption. You simply reinitialize the RC4 cipher with the same secret key and apply the keystream to the ciphertext using the XOR operation to obtain the original plaintext.

### Algorithm:
1. Key Scheduling Algorithm (KSA): Initialize the RC4 cipher with the secret key, which is typically a permutation of all 256 possible bytes.
2. Pseudorandom Generation Algorithm (PRGA): Generate a keystream of the same length as the plaintext by repeatedly generating pseudorandom bytes based on the state of the RC4 cipher.

#### Example:
- Plaintext: "HELLO WORLD"
- Key: "SECRET"
- Encrypted text: "URHGC\x1dI\x17\x00\x03aE\x0c"

The RC4 Cipher is widely used in various cryptographic protocols and applications, including SSL/TLS for secure communication over the internet.

![image](https://gist.github.com/assets/40488244/bfbedc38-c401-4f0f-9162-dee8a40db997)

```
# Harry Sauers
# rc4.py
# demo of RC4 encryption algorithm


def key_scheduling(key):
    sched = [i for i in range(0, 256)]
    
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
    return sched
    

def stream_generation(sched):
    stream = []
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
        yield sched[(sched[i] + sched[j]) % 256]        


def encrypt(text, key):
    text = [ord(char) for char in text]
    key = [ord(char) for char in key]
    
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    
    ciphertext = ''
    for char in text:
        enc = str(hex(char ^ next(key_stream))).upper()
        ciphertext += (enc)
        
    return ciphertext
    

def decrypt(ciphertext, key):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    
    plaintext = ''
    for char in ciphertext:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec
    
    return plaintext


if __name__ == '__main__':
    ed = input('Enter E for Encrypt, or D for Decrypt: ').upper()
    if ed == 'E':
        plaintext = input('Enter your plaintext: ')
        key = input('Enter your secret key: ')
        result = encrypt(plaintext, key)
        print('Result: ')
        print(result)
    elif ed == 'D': 
        ciphertext = input('Enter your ciphertext: ')
        key = input('Enter your secret key: ')
        result = decrypt(ciphertext, key)
        print('Result: ')
        print(result)
    else:
        print('Error in input - try again.')

```

## 6. Playfair Cipher

The Playfair cipher is a manual symmetric encryption technique that was invented in 1854 by Charles Wheatstone. It employs a 5x5 grid of letters, called a Playfair square, to encrypt pairs of letters in the plaintext.

### Description:
- The Playfair cipher encrypts pairs of letters (digraphs) rather than individual letters.
- It uses a 5x5 grid of letters, typically excluding the letters 'J' (replaced by 'I') and 'Q' (usually combined with 'U').
- Each letter of the plaintext is replaced by another letter according to the rules of the Playfair square.

### Encryption:
1. Generate a Playfair square based on a keyword (ignoring duplicate letters and 'J').
2. Break the plaintext into digraphs (pairs of letters), padding with an extra letter if necessary.
3. For each digraph, apply the following rules:
   - If the two letters are in the same row, replace them with the letters to their immediate right, wrapping around if necessary.
   - If the two letters are in the same column, replace them with the letters immediately below them, wrapping around if necessary.
   - If the letters form a rectangle, replace them with the letters at the opposite corners of the rectangle.
   - If the letters are different and do not form a rectangle, form a rectangle with the letters and replace them with the letters on the same row but opposite corners of the rectangle.
4. The resulting digraphs form the ciphertext.

### Decryption:
1. Generate the same Playfair square based on the same keyword.
2. For each digraph in the ciphertext, apply the reverse transformation using the rules described above to obtain the original plaintext.

### Algorithm:
1. Generate a Playfair square based on the keyword, ignoring duplicate letters and 'J'.
2. Break the plaintext into digraphs and apply the encryption rules to each digraph.
3. For decryption, generate the same Playfair square based on the keyword and apply the reverse transformation to each digraph in the ciphertext.

#### Example:
- Plaintext: "HELLO WORLD"
- Keyword: "PLAYFAIR"
- Encrypted text: "XDWZVYCXOVB"

The Playfair cipher provides a manual method of encryption that was widely used before the advent of computers. It offers a more secure alternative to simple substitution ciphers.


![image](https://gist.github.com/assets/40488244/6f1986aa-320d-4547-8cf3-1e5ff7e0a50b)

```
#CONTACT FOR ANY QUESTIONS
#CODERATRI-ATRISAXENA2@GMAIL.COM
#See this example: https://www.javatpoint.com/playfair-cipher-program-in-java

key=input("Enter key")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: #storing key
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Encryption
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
        
  ```






