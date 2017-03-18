"""
Sum of Two Values

find_sum_of_two_2 function returns True if there are two values in array
who sum to value and returns False otherwise.

This solution works only if data is sorted.
Does not require extra memory
"""


def find_sum_of_two_2(array, val):
    min_index = 0
    max_index = len(array) - 1
    while min_index < max_index:
        intermediate_sum = array[min_index] + array[max_index]
        if intermediate_sum == val:
            return True

        if intermediate_sum < val:
            min_index += 1
        else:
            max_index -= 1

    return False
