"""
Given an integer array, move all elements containing '0' to the left
while maintaining the order of other elements in the array.
"""


def move_zeros_to_left(array):
    if len(array) < 1:
        return

    length_a = len(array)
    write_index = length_a - 1
    read_index = length_a - 1

    while read_index >= 0:
        if array[read_index] != 0:
            array[write_index] = array[read_index]
            write_index -= 1

        read_index -= 1

    while write_index >= 0:
        array[write_index] = 0
        write_index -= 1
