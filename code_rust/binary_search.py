"""
Binary Search
"""


def binary_search_recur(array, key, low, high):
    if low > high:
        return -1

    mid = low + ((high - low) // 2)
    if array[mid] == key:
        return mid
    elif key < array[mid]:
        return binary_search_recur(array, key, low, mid - 1)
    else:
        return binary_search_recur(array, key, mid + 1, high)


def binary_search(array, key):
    return binary_search_recur(array, key, 0, len(array) - 1)


def binary_search_iter(array, key):
    low = 0
    high = len(array)

    while low <= high:
        mid = low + ((high - low) // 2)
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # Not found


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(binary_search(a, 5))
    print(binary_search_iter(a, 5))
