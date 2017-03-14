"""
Search Rotated Array
"""


def search_rotated(array, key, start, end):
    if start > end:
        return -1

    mid = start + ((end - start) // 2)
    if array[mid] == key:
        return mid

    elif (array[start] < array[mid] and
          key < array[mid] and
          key >= array[start]):
        return search_rotated(array, key, start, mid - 1)

    elif (array[mid] < array[end] and
          key > array[mid] and
          key <= array[end]):
        return search_rotated(array, key, mid + 1, end)

    elif array[start] > array[mid]:
        return search_rotated(array, key, start, mid - 1)

    elif array[end] < array[mid]:
        return search_rotated(array, key, mid + 1, end)

    return -1


def binary_search_rotated(arr, key):
    return search_rotated(arr, key, 0, len(arr) - 1)
