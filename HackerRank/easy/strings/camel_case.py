"""
Given string camelCase string s, print the number of words in s on a new line
"""


def count_words_in_camel_case(st):
    upper_chars = [char for char in st if char.isupper()]
    total_words = len(upper_chars) + 1
    return total_words

if __name__ == '__main__':
    st = input().strip()
    print(count_words_in_camel_case(st))
