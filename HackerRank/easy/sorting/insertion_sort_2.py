"""
Full Insertion Sort
"""

# n = int(input())
# arr = [int(s) for s in input().strip().split(" ")]


def insertion_sort(arr):
    for i, x in enumerate(arr[1:], 1):
        position = i
        while position > 0 and x < arr[position - 1]:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = x
        print(" ".join([str(r) for r in arr]))
    return arr
