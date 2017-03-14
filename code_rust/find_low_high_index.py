"""
Find Low/High Index
"""


def find_low_index(array, key):
    low = 0
    high = len(array) - 1
    mid = high // 2

    while low <= high:
        if key < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

        mid = low + ((high - low) // 2)

    if array[low] == key:
        return low
    return -1


def find_high_index(array, key):
    low = 0
    high = len(array) - 1
    mid = high // 2

    while low <= high:
        if key <= array[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = low + (high - low) // 2

    if array[high] == key:
        return high
    return -1
