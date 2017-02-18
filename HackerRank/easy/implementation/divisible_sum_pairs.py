"""
You are given an array of n integers and a positive integer k.
Find and print the number of (i, j) pairs where i < j and ai + aj
is evenly divisible by k.
"""


def main(a, k):
    i = 0
    count = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if i < j and (a[i] + a[j]) % k == 0:
                count += 1
            j += 1
        i += 1
    return count

if __name__ == '__main__':
    n, k = input().strip().split(" ")
    n, k = int(n), int(k)
    a = [int(a_temp) for a_temp in input().strip().split(" ")]
    print(main(a, k))
