"""
https://www.hackerrank.com/challenges/caesar-cipher-1?h_r=next-challenge&h_v=zen
"""


def caesar_cipher(unencrypted_string, rotation):
    encrypted_string = ""
    for char in unencrypted_string:
        if not char.isalpha():
            encrypted_string += char
            continue
        base = "a" if char.islower() else "A"
        encrypted_string += chr((ord(char) + rotation - ord(base)) % 26 + ord(base))
    return encrypted_string


if __name__ == '__main__':
    n = int(input().strip())
    unencrypted_string = input().strip()
    k = int(input().strip())
    print(caesar_cipher(unencrypted_string, k))
