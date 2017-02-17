"""
Given the starting locations and movement rates for each kangaroo,
can you determine if they'll ever land at the same location at the same time?
"""

x1, v1, x2, v2 = input().strip().split(" ")
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

while x1 <= x2:
    if x1 == x2:
        print("YES")
        break
    elif x2 > x1 and v2 >= v1:
        break
    else:
        x1 += v1
        x2 += v2
if x1 != x2:
    print("NO")


# Other Solution
def solve(x1, v1, x2, v2):
    if x1 > x2: return solve(x2, v2, x1, v1)
    if x1 == x2: return True
    if v1 <= v2: return False
    return (x1-x2) % (v2-v1) == 0


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
print "YES" if solve(x1, v1, x2, v2) else "NO"
