def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    first_lower_letter_code = ord('a')
    first_upper_letter_code = ord('A')
    length = 26

    n = len(plaintext)
    text_codes = [ord(plaintext[i]) for i in range(n)]

    m = len(keyword)
    key_codes = [ord(keyword[i]) for i in range(m)]
    for i in range(m):
        if keyword[i].isupper():
            key_codes[i] -= first_upper_letter_code
        else:
            key_codes[i] -= first_lower_letter_code

    for i in range(n):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                text_codes[i] = (text_codes[i] - first_upper_letter_code + key_codes[i % m]) % length + first_upper_letter_code
            else:
                text_codes[i] = (text_codes[i] - first_lower_letter_code + key_codes[i % m]) % length + first_lower_letter_code

    for i in range(n):
        ciphertext += chr(text_codes[i])
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    first_lower_letter_code = ord('a')
    first_upper_letter_code = ord('A')
    length = 26

    n = len(ciphertext)
    text_codes = [ord(ciphertext[i]) for i in range(n)]

    m = len(keyword)
    key_codes = [ord(keyword[i]) for i in range(m)]
    for i in range(m):
        if keyword[i].isupper():
            key_codes[i] -= first_upper_letter_code
        else:
            key_codes[i] -= first_lower_letter_code

    for i in range(n):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                text_codes[i] = (text_codes[i] - first_upper_letter_code - key_codes[i % m] + length) % length + first_upper_letter_code
            else:
                text_codes[i] = (text_codes[i] - first_lower_letter_code - key_codes[i % m] + length) % length + first_lower_letter_code

    for i in range(n):
        plaintext += chr(text_codes[i])

    return plaintext