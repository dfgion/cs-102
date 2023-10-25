def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for symbol in plaintext:
        if symbol == 'X':
            ciphertext += 'A'
        elif symbol == 'Y':
            ciphertext += 'B'
        elif symbol == 'Z':
            ciphertext += 'C'
        else:
            ciphertext+=chr(ord(symbol)+shift)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for symbol in ciphertext:
        if symbol == 'A':
            plaintext += 'X'
        elif symbol == 'B':
            plaintext += 'Y'
        elif symbol == 'C':
            plaintext += 'Z'
        else:
            plaintext+=chr(ord(symbol)-shift)
    return plaintext
print(ord('Z'))
print(encrypt_caesar('PYTHON'))
print(decrypt_caesar('SBWKRQ'))