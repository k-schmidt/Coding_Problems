"""
https://leetcode.com/problems/nim-game/?tab=Solutions
"""


class Solution(object):

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
