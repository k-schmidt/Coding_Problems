"""
https://leetcode.com/problems/find-the-difference/?tab=Description
"""
import operator


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                break
            i += 1
        return sorted_t[i]


class SolutionXOR(object):
    def findTheDifference(self, s, t):
        return chr(reduce(operator.xor, map(ord, s + t)))


class SolutionZip(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_t[-1] if sorted_s == sorted_t[:-1] else [b
                                                               for a, b
                                                               in zip(sorted_s,
                                                                      sorted_t)
                                                               if a != b][0]
