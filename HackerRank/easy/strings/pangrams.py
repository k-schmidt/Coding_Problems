"""
https://www.hackerrank.com/challenges/pangrams
"""


def is_pangram(sentence):
    alphabet = set(["a", "b", "c", "d", "e", "f",
                    "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u",
                    "v", "w", "x", "y", "z"])
    uniq_chars = set()
    for char in sentence:
        lower_char = char.lower()
        if lower_char == " ":
            continue
        uniq_chars.add(lower_char)
    return "pangram" if uniq_chars == alphabet else "not pangram"

if __name__ == '__main__':
    sentence = input().strip()
    print(is_pangram(sentence))
