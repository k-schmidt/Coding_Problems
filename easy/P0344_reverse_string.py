"""
Write a function that takes a string as input and returns
the string reversed.

Example:
Given s = "hello", return "olleh"
"""


# First Pass Recursive Solution - Memory Exceeded
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        else:
            return s[-1] + self.reverseString(s[1:-1]) + s[0]


# Second Pass - Time Exceeded
class SecondSolution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        st_out = ""
        for char in s:
            stack.append(char)

        while stack:
            st_out += stack.pop()
        return st_out


# Solution Three - Accepted
class ThirdSolution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        i = 0
        j = -1
        str_list = list(s)

        while i < len(str_list) / 2:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
        return "".join(str_list)


# Other Solutions
def reverseString(self, s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]
