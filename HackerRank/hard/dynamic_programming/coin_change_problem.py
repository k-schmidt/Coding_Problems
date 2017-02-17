"""
How many different ways can you make change for an amount,
given a list of coins?

If you think of a way to store the checked solutions,
then this store can be uses to avoid checking the
same solution again and again.

Sample Input:
4 3
1 2 3

Sample Output:
4

Hints:
Think about the degenerate cases:
  1. How many ways can you give change for 0 cents?
  2. How many ways can you give change for > 0 cents,
     if you have no coins?
"""

n, _ = input().split()
n = int(n)
coins = [int(c) for c in input().split()]

change_counter = [0] * (n + 1)

# There is one way to make no change, choose no coins.
change_counter[0] = 1

for coin in coins:
    for x in range(coin, n + 1):
        change_counter[x] += change_counter[x - coin]
print(change_counter[n])
