"""
https://www.hackerrank.com/challenges/bon-appetit
"""


def compute_anna_portion(prices, k):
    return sum((price for i, price in enumerate(prices) if i != k)) / 2


def main(k, prices, charged):
    a_portion = compute_anna_portion(prices, k)
    if charged - a_portion == 0:
        return "Bon Appetit"
    return charged - a_portion

if __name__ == '__main__':
    n, k = input().strip().split(" ")
    n, k = int(n), int(k)
    prices = [int(a_temp) for a_temp in input().strip().split(" ")]
    charged = int(input().strip())
    main(k, prices, charged)
