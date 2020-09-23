
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
            if (char) > ascii_max - 1:
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
    ascii_max = 91 
    alphabet_shift = 26
    vigenere_encrypt = ""

    encrypt_string = vigenere_get_key_phrase(len(plaintext), keyword)
    current_plain_index = 0
    for letter in encrypt_string:
        shift = vigenere_getshift(plaintext[current_plain_index])
        char = ord(letter) + shift

        if (char) > ascii_max - 1:
            char = char - alphabet_shift

        vigenere_encrypt = vigenere_encrypt + chr(char)
        current_plain_index = current_plain_index + 1

    return vigenere_encrypt
            

# Arguments: string
# Returns: integer
def vigenere_getshift(shiftchar):
    ascii_min = 65
    shift = ord(shiftchar) - ascii_min
    return shift


# Arguments: integer, string
# Returns: string
def vigenere_get_key_phrase(plain_length, keyword):
    key_encrypt = ""
    key_index = 0

    while len(key_encrypt) < plain_length:
        if key_index > len(keyword) - 1:
            key_index = 0

        key_encrypt = key_encrypt + keyword[key_index]

        key_index = key_index + 1

    return key_encrypt


# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypt = ""

    actualkeyword = ""

    i = 0
    for char in ciphertext:
        actualkeyword = actualkeyword + keyword[i]
        if(i == len(keyword) - 1): 
            i = -1
        i = i + 1

    i = 0

    for char in ciphertext:
        letter = ord(char) - ord(actualkeyword[i]) + 65
        if(letter < 65):
            letter = letter + 26
        decrypt = decrypt + chr(letter)
        i = i + 1

    return decrypt

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):

    W = [total]
    total = total + w[0]
    i = 1
    while i < n:
    	total = total + W[i]
    	W = W + [random.range(total + 1, 2 * total)]

    Q = random.randint((total + 1, 2 * total))
    while 1 == 1:         
    	R = random.randint(2, Q-1)         
    	if math.gcd(R,Q) == 1:             
    		break      
    return (W, Q, R) 

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
    vigenere_encrypt_string = encrypt_vigenere("ATTACKATDAWN","LEMON")
    print(vigenere_encrypt_string)
    print(decrypt_vigenere(vigenere_encrypt_string,"LEMON"))
    print(generate_private_key(n=8))

if __name__ == "__main__":
    main()
