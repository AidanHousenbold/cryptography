
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    ascii_min = 64
    ascii_max = 91 
    alphabet_shift = 26
    encrypt = ""
    for letter in plaintext:
        current = ord(letter)
        if current > ascii_min and current < ascii_max:
            char = ord(letter) + offset
            if (char) > ascii_max + 1:
                char = char - alphabet_shift
            current = char

        encrypt = encrypt + chr(current)
 
    return encrypt

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    ascii_min = 64
    ascii_max = 91 
    alphabet_shift = 26
    decrypt = ""
    for letter in ciphertext:
        current = ord(letter)
        if current > ascii_min and current < ascii_max:
            char = ord(letter) - offset
            if (char) < ascii_min + 1:
                char = char + alphabet_shift
            current = char

        decrypt = decrypt + chr(current)
 
    return decrypt

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():

    encrypt_string = encrypt_caesar("PYTHON CLUB.", 3)
    print(encrypt_string)
    print(decrypt_caesar(encrypt_string, 3))
    

if __name__ == "__main__":
    main()
