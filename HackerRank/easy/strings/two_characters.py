"""
https://www.hackerrank.com/challenges/two-characters
"""
from itertools import combinations


def get_uniq_chars(st):
    return set(st)


def check_t(t_str):
    t = True
    i = 0
    while i < len(t_str) - 1:
        if t_str[i] == t_str[i + 1]:
            t = False
            break
        else:
            i += 1
    return len(t_str) if t else 0


def main(s_str):
    uniq_chars = get_uniq_chars(s_str)
    return max([check_t("".join(st
                                for st
                                in s_str
                                if st not in char_combo))
                for char_combo
                in combinations(uniq_chars, len(uniq_chars) - 2)])

if __name__ == '__main__':
    n = int(input().strip())
    s_str = input().strip()
    print(main(s_str))
