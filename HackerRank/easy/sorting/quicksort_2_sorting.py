"""
https://www.hackerrank.com/challenges/quicksort2?h_r=next-challenge&h_v=zen
"""


def partition(arr, pivot, lower_array, higher_array):
    if len(arr) == 0:
        return
    else:
        lower_array.append(arr[0]) if arr[0] < pivot else higher_array.append(arr[0])
        print(lower_array, " | ", higher_array)
        partition(arr[1:], pivot, lower_array, higher_array)
