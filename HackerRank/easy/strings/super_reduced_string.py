"""
Reduce string as much as possible

Sample input
aaabccddd

Sample Output
abd

Sample Input
baab

Sample Output
Empty String
"""


def reduce_string(st):
    i = 0
    while i < len(st[:-1]):
        if st[i + 1] == st[i]:
            st = st[:i] + st[i+2:]
            i = 0
        else:
            i += 1
    return st if st else "Empty String"


def reduce_string_2(st):
    while True:
        for i in range(len(st) - 1):
            if st[i] == st[i + 1]:
                st = st[:i] + st[i+2:]
                break
        else:
            break
    return st if st else "Empty String"

if __name__ == '__main__':
    st = input().strip()
    print(reduce_string(st))
    print(reduce_string_2(st))
