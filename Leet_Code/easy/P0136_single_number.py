"""
https://leetcode.com/problems/single-number/?tab=Description
"""
from functools import reduce
from operator import xor


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(xor, nums)
