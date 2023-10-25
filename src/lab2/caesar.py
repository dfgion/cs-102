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
    upper = False
    for symbol in plaintext:
        if ((ord(symbol.upper())>64) and (ord(symbol.upper())< 91)):
            if symbol.isupper():
                upper = True
            symbol = symbol.upper()
            number = ord(symbol)+shift if (ord(symbol)+shift)<91 else 64+(ord(symbol)+shift)-90
            if upper == True:
                ciphertext += chr(number)
            else:
                ciphertext += chr(number).lower()
            upper = False
        else:
            ciphertext += symbol
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
    upper = False
    for symbol in ciphertext:
        if ((ord(symbol.upper())>64) and (ord(symbol.upper())< 91)):
            if symbol.isupper():
                upper = True
            symbol = symbol.upper()
            number = ord(symbol)-shift if (ord(symbol)-shift)>64 else 91-(-(ord(symbol)-shift)+65)
            if upper == True:
                plaintext += chr(number)
            else:
                plaintext += chr(number).lower()
            upper = False
        else:
            plaintext += symbol
    return plaintext
print(encrypt_caesar('Sbwkrq3.6'))
print(decrypt_caesar('Veznut3.6'))