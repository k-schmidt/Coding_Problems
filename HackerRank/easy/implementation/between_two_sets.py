"""
Consider two sets of positive integers, A and B.
We say that a positive integer, x, is between sets A and B
if the following conditions are satisfied:

1. All elements in A are factors of x.
2. x is a factor of all elements in B.

Given A and B, find and print the number of integers that are
between the two sets.
"""
from functools import reduce


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) / gcd(x, y)


def main(a, b):
    count = 0
    lcm_a = reduce(lcm, a)
    i = lcm_a
    while i <= min(b):
        if all((x % i == 0 for x in b)):
            count += 1
        i += lcm_a
    return count

if __name__ == '__main__':
    n, m = input().strip().split(" ")
    n, m = int(n), int(m)
    a = [int(a_temp) for a_temp in input().strip().split(" ")]
    b = [int(b_temp) for b_temp in input().strip().split(" ")]
    main(a, b)
