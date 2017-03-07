"""
https://www.hackerrank.com/challenges/countingsort1
"""


def count_observations(nums):
    obs = [0] * len(nums)
    for n in nums:
        obs[n] += 1
    return obs

if __name__ == '__main__':
    n = int(input().strip())
    nums = [int(i) for i in input().split()]
    obs = count_observations(nums)
    print(" ".join([str(i) for i in obs if i]))
