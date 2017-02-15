"""
Given a positive integer, output its complement number. The complement strategy
is to flip the bits of its binary representation.

Note:
1. The given integer is guaranteed to fit
   within the range of a 32-bit signed integer.
2. You could assume no leading zero bit in the integer's binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
             and its complement is 010. So you need to output 2

Example 2:
Input: 1
Ouput: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits),
             and its complement is 0. So you need to output 0
"""


# First pass
# O(lgn) ??
class Solution:
    def rebase(self, num, base):
        conversion = ["0", "1", "2", "3", "4", "5",
                      "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        if num < base:
            return conversion[base]
        else:
            return self.rebase(num // base, base) + conversion[num % base]

    def compute_complement(self, bin_n):
        if len(bin_n) == 1:
            comp = "1" if bin_n[0] == "0" else "0"
            return comp
        else:
            comp = "1" if bin_n[0] == "0" else "0"
            return comp + self.compute_complement(bin_n[1:])

    def int_to_bin(self, bin_str):
        exp = 0
        sm = 0
        while bin_str:
            if int(bin_str[-1]) == 1:
                sm += 2 ** exp
            bin_str = bin_str[:-1]
            exp += 1
        return sm

    def findComplement(self, num):
        bin_n = self.rebase(num, 2)
        comp = self.compute_complement(bin_n)
        return self.int_to_bin(comp)


# Other Solutions
class Solution2:
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

if __name__ == '__main__':
    print(Solution().findComplement(5))
    print(Solution2().findComplement(5))
