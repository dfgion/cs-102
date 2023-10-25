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
    correct_kw = ""
    checker = 0
    for symbol in range(len(plaintext)):
        if checker > (len(keyword)-1):
            checker = 0
            correct_kw += keyword[checker]
            checker +=1
        else:
            correct_kw += keyword[checker]
            checker += 1
    ciphertext = ""
    upper = False
    for index in range(len(plaintext)):
        if ((ord(plaintext[index].upper())>64) and (ord(plaintext[index].upper())< 91)):
            if plaintext[index].isupper():
                upper = True
            number = ord(plaintext[index].upper())+(ord(correct_kw[index].upper())-65) if (ord(plaintext[index].upper())+(ord(correct_kw[index].upper())-65)) < 91 else (ord(plaintext[index].upper())+(ord(correct_kw[index].upper())-65))-90+64
            if upper == True:
                ciphertext += chr(number) 
            else:
                ciphertext += chr(number).lower()
            upper = False
        else:
            ciphertext += plaintext[index]
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
    correct_kw = ""
    checker = 0
    for symbol in range(len(ciphertext)):
        if checker > (len(keyword)-1):
            checker = 0
            correct_kw += keyword[checker]
            checker +=1
        else:
            correct_kw += keyword[checker]
            checker += 1
    upper = False
    plaintext = ""
    for index in range(len(ciphertext)):
        if ((ord(ciphertext[index].upper())>64) and (ord(ciphertext[index].upper())< 91)):
            if ciphertext[index].isupper():
                upper = True
            number = ord(ciphertext[index].upper())-(ord(correct_kw[index].upper())-65) if (ord(ciphertext[index].upper())-(ord(correct_kw[index].upper())-65)) > 64 else 91-(-(ord(ciphertext[index].upper())-(ord(correct_kw[index].upper())-65))+65)
            if upper == True:
                plaintext += chr(number) 
            else:
                plaintext += chr(number).lower()
            upper = False
        else:
            plaintext += ciphertext[index]
    return plaintext
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
print(decrypt_vigenere("PYTHON", "A"))