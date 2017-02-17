"""
Given a sorted list with an unsorted e in the rightmost cell, can you write
some simple code to insert e into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array
is fully sorted. The goal of this challenge is to follow the correct
order of insertion sort.

Guideline:
You can copy the value of e to a variable and consider its cell "empty".
Since this leaves an extra cell empty on the right, you can shift everything
over until V can be inserted.
This will create duplicates of each value, but when you reach the right spot,
you can replace it with e.
"""

n = int(input())
arr = [int(i) for i in input().split()]

e = arr[-1]
j = arr.index(e) - 1
while e < arr[j] and arr.index(e) > 0:
    arr[j + 1] = arr[j]
    print(" ".join([str(x) for x in arr]))
    arr[j] = e
    j -= 1
arr[j + 1] = e
print(" ".join([str(x) for x in arr]))
