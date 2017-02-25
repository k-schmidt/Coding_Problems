"""
https://www.hackerrank.com/challenges/runningtime?h_r=next-challenge&h_v=zen
"""


def insertion_sort(arr):
    count = 0
    for i, elem in enumerate(arr[1:], 1):
        j = i - 1
        while (j >= 0) and (arr[j] > elem):
            arr[j + 1] = arr[j]
            count += 1
            j -= 1
        arr[j+1] = elem
    return count


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    print(insertion_sort(arr))
