"""
Given an array of integers, rotate the array by 'N' elements.
"""


def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array_in_place(arr, n):
    length_arr = len(arr)

    # Let's normalize rotations
    # If n > array size or n is negative
    n = n % length_arr
    if n < 0:
        # Calculate the positive rotations needed.
        n += length_arr

    # Let's partition the array base on rotations 'n'.
    # For example: 1, 2, 3, 4, 5 where n = 2
    # -> 5, 4, 3, 2, 1
    # -> 4, 5, 3, 2, 1
    # -> 4, 5, 1, 2, 3

    reverse_array(arr, 0, length_arr - 1)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, n, length_arr - 1)
