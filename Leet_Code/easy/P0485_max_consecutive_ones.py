"""
https://leetcode.com/problems/max-consecutive-ones/?tab=Description
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_consecutive = 0
        global_consecutive = 0
        for i, num in enumerate(nums):
            if num == 1:
                current_consecutive += 1
                if current_consecutive > global_consecutive:
                    global_consecutive = current_consecutive
            else:
                current_consecutive = 0
        return global_consecutive


class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        current_consecutive = 0
        global_consecutive = 0
        for num in nums:
            if num == 1:
                current_consecutive += 1
                global_consecutive = max(global_consecutive,
                                         current_consecutive)
            else:
                current_consecutive = 0
        return global_consecutive
