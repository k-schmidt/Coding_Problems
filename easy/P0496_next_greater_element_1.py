"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1
elements are a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding
places of nums2.

The next greater number of a number x in nums1 is the first greater number
 to its right in nums2. If it doesn't exist, output -1 for this number

Example 1:
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]

Example 2:
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
"""

# First pass
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        stack = []
        hash_dict = {}
        for x in nums:
            while len(stack) and stack[-1] < x:
                hash_dict[stack.pop()] = x
            stack.append(x)

        for x in findNums:
            output.append(hash_dict.get(x, -1))
        return output

# Other solutions
def nextGreaterElement(self, findNums, nums):
    return [next((y
                  for y in nums[nums.index(x):]
                  if y > x), -1)
            for x in findNums]
