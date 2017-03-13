"""
https://www.hackerrank.com/challenges/countingsort4
"""


def organize_input(n):
    result = []
    for x in range(n):
        num, char = [i for i in input().split()]
        num, char = int(num), str(char)
        if x < n // 2:
            result.append((num, char, "-"))
        else:
            result.append((num, char, char))
    return result

if __name__ == '__main__':
    n = int(input().strip())
    result = organize_input(n)
    sorted_result = sorted(result, key=lambda tup: tup[0])
    print(" ".join([x for _, _, x in sorted_result]))
