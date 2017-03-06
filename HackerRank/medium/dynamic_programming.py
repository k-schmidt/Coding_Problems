"""
https://www.hackerrank.com/challenges/equal
"""


def main(n, ways):
    for x in range(n):
        num_emp = input().strip()
        emps = sorted([int(i) for i in input().split()])

        # Case 1
        min_chocolate = min(emps)
        target = [min_chocolate] * len(emps)
        delta = [a - b for a, b in zip(emps, target)]
        min_ops_1 = 0
        for d in delta:
            min_ops_1 += (d // 5) + ((d % 5) // 2) + (((d % 5) % 2) // 1)

        # Case 2
        min_chocolate = 0
        target = [min_chocolate] * len(emps)
        delta = [a - b for a, b in zip(emps, target)]
        min_ops_0 = 0
        for d in delta:
            min_ops_0 += (d // 5) + ((d % 5) // 2) + (((d % 5) % 2) // 1)

        return min(min_ops_0, min_ops_1)

if __name__ == '__main__':
    n = int(input().strip())
    ways = [5, 2, 1]
    print(main(n, ways))
