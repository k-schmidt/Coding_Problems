"""
Peaks and Valleys
"""
import sys


def max_index(array, a, b, c):
    length = len(array)
    a_val = array[a] if a >= 0 and a < length else -sys.maxint - 1
    b_val = array[b] if b >= 0 and b < length else -sys.maxint - 1
    c_val = array[c] if c >= 0 and c < length else -sys.maxint - 1

    m = max(a_val, max(b_val, c_val))
    if a_val == m:
        return a
    elif b_val == m:
        return b
    else:
        return c


def sort_valley_peak(array):
    i = 1
    while i < len(array):
        biggest_index = max_index(array, i - 1, i, i + 1)
        if i != biggest_index:
            array[i], array[biggest_index] = array[biggest_index], array[i]
        i += 2
