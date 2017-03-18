"""
Given a large array of integers and a window of size 'w',
find the current maximum in the window as the window slides through the entire array.
"""
from collections import deque


def find_max_sliding_window(arr, window_size):
    if window_size > len(arr):
        return

    window = deque()

    # Find out max for first window
    for i in range(window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)

    print(arr[window[0]])

    for i in range(window_size, len(arr)):
        # Remove all numbers that are smaller than the current number
        # from the tail of list
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        # Remove first number if it doesn't fall in the window anymore
        if window and (window[0] <= i - window_size):
            window.popleft()

        window.append(i)
        print(arr[window[0]])
