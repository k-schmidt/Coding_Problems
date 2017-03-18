"""
Merge Overlapping Intervals
"""


def find_busy_intervals(array):
    if len(array) == 0:
        return None

    merged_array = []
    merged_array.append(array[0][0], array[0][1])

    for i in range(1, len(array)):
        x1 = array[i][0]
        y1 = array[i][1]
        y2 = merged_array[-1][1]

        if y2 >= x1:
            merged_array[-1][1] = max(y1, y2)
        else:
            merged_array.append((x1, y1))

    return merged_array
