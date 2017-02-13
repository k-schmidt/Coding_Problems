"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1 = (0 0 0 1)
4 = (0 1 0 0)
"""
from typing import List, Union


def convert_to_base(n: int, base: int) -> List[Union[int, str]]:
    conversion = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                  "A", "B", "C", "D", "E", "F"]
    if n < base:
        return [n]
    return convert_to_base(n // base, base) + [conversion[n % base]]


def comparison(input1: int, input2: int) -> int:
    return bin(input1 ^ input2).count('1')

if __name__ == '__main__':
    print("Calling with 1 and 4: ", comparison(1, 4))
    print("Calling with 10 and 8: ", comparison(10, 8))
