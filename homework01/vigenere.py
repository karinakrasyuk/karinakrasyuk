def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = keyword
    while len(key) < len(plaintext):   
        key += keyword

    for i in range(0, len(plaintext)):
        c = plaintext[i]   
        shift = None       
        if key[i].isupper():    
            shift = ord(key[i]) - ord('A')
        else:
            shift = ord(key[i]) - ord('a')

        if c.isalpha():  
            mesto = ord(c)
            if c.isupper():  
                k = ord('A')
            else:
                k = ord('a')

            new_mesto = k + (mesto + shift - k) % 26
            ciphertext += chr(new_mesto)
        else:
            ciphertext += c  
            
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = keyword
    while len(key) < len(ciphertext):
        key += keyword

    for i in range(0, len(ciphertext)):
        c = ciphertext[i]

        shift = None
        if key[i].isupper():
            shift = ord(key[i]) - ord('A')
        else:
            shift = ord(key[i]) - ord('a')


        if c.isalpha():  
            mesto = ord(c)
            if c.isupper():  
                k = ord('A')
            else:
                k = ord('a')

            new_mesto = k + (mesto - shift - k + 26) % 26
            plaintext += chr(new_mesto)
        else:
            plaintext += c  
    
    return plaintext
