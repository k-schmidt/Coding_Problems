"""
https://www.hackerrank.com/challenges/closest-numbers
"""


def find_closest(arr):
    sorted_arr = sorted(arr)
    smallest_diff = [sorted_arr[0], sorted_arr[1]]
    mn = sorted_arr[1] - sorted_arr[0]
    for i, j in enumerate(sorted_arr[2:], 2):
        diff = j - sorted_arr[i - 1]
        if abs(diff) < mn:
            smallest_diff = []
            smallest_diff.append(sorted_arr[i - 1])
            smallest_diff.append(j)
            mn = abs(diff)
        elif abs(diff) == mn:
            smallest_diff.append(sorted_arr[i - 1])
            smallest_diff.append(j)
    return smallest_diff

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().split()]
    print(" ".join([str(i) for i in find_closest(arr)]))
