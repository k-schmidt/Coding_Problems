"""
Given five positive integers,
find the minimum and maximum values that can be calculated
by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a
single line of two space-separated long integers.

Input Format
A single line of five space-separated integers.

Constraints
Each integer is in the inclusive range [0, 10^9]

Output Format
Print two space-separated long integers denoting the respective
minimum and maximum values that can be calculated by summing
exactly four of the five integers.
(The output can be greater than 32 bit integer.)

Sample Input
1 2 3 4 5

Sample Output
10 14
"""


def main(input_list):
    total_sum = sum(input_list)

    for i, x in enumerate(input_list):
        if i == 0:
            min_sum = total_sum - x
            max_sum = total_sum - x
        else:
            if total_sum - x < min_sum:
                min_sum = total_sum - x
            if total_sum - x > max_sum:
                max_sum = total_sum - x
    return min_sum, max_sum

# Other Solution
a = sorted(map(int,raw_input().split()))
print sum(a[:4]),sum(a[1:])
