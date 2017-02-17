"""
When a fruit falls from its tree, it lands units of distance from
its tree of origin along the -axis.
A negative value of means the fruit fell units to the tree's left,
and a positive value of means it falls units to the tree's right.

Given the value of for apples and oranges,
can you determine how many apples and oranges will fall on Sam's
house (i.e., in the inclusive range )?
Print the number of apples that fall on Sam's house as your first
line of output, then print the number of oranges that fall on Sam's
house as your second line of output.
"""
# SetUp
s, t = input().strip().split(" ")
s, t = [int(s), int(t)]
a, b = input().strip().split(" ")
a, b = [int(a), int(b)]
m, n = input().strip().split(" ")
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().stip().split(" ")]
orange = [int(orange_temp) for orange_temp in input().strip().split(" ")]

# Logic
sam_apple = len(list(filter(lambda x: x + a >= s and x + a <= t, apple)))
sam_orange = len(list(filter(lambda x: x + a >= s and x + a <= t, orange)))
print(sam_apple)
print(sam_orange)
