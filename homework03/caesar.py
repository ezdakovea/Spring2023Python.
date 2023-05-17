import typing as tp
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    first_lower_letter_code = ord('a')
    first_upper_letter_code = ord('A')
    alphLen = 26
    n = len(plaintext)
    codes = [ord(plaintext[i]) for i in range(n)]
    for i in range(n):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                codes[i] = (codes[i] - first_upper_letter_code + shift) % alphLen + first_upper_letter_code
            else:
                codes[i] = (codes[i] - first_lower_letter_code + shift) % alphLen + first_lower_letter_code
    for i in range(n):
        ciphertext += chr(codes[i])

    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    first_lower_letter_code = ord('a')
    first_upper_letter_code = ord('A')
    alphLen = 26
    n = len(ciphertext)
    codes = [ord(ciphertext[i]) for i in range(n)]
    for i in range(n):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                codes[i] = (codes[i] - first_upper_letter_code - shift + alphLen) % alphLen + first_upper_letter_code
            else:
                codes[i] = (codes[i] - first_lower_letter_code - shift + alphLen) % alphLen + first_lower_letter_code
    for i in range(n):
        plaintext += chr(codes[i])
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift