"""
https://www.hackerrank.com/challenges/quicksort1?h_r=next-challenge&h_v=zen
"""
from itertools import chain


def partition(arr):
    partition_key = arr[0]
    lower_array = []
    equal_array = []
    higher_array = []
    for char in arr:
        if char < partition_key:
            lower_array.append(char)
        elif char == partition_key:
            equal_array.append(char)
        else:
            higher_array.append(char)
    for char in chain(lower_array,
                      equal_array,
                      higher_array):
        print(char, end=" ")


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    partition(arr)
